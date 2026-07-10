from __future__ import annotations

import base64
import io
import math
import os
import tempfile
from dataclasses import dataclass
from typing import Any

import cadquery as cq
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image, ImageDraw, ImageFont
from pydantic import BaseModel, ConfigDict, Field


app = FastAPI(
    title="Raised Bed CAD Geometry Engine",
    version="3.0.0",
    description="Generates raised-bed CAD files and true 3D preview images.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


INCH_MM = 25.4
FOOT_MM = 12.0 * INCH_MM

WOOD_THICKNESS_MM = 1.5 * INCH_MM       # actual 2x lumber thickness
WOOD_BOARD_WIDTH_MM = 11.25 * INCH_MM   # actual 2x12 width
POST_MM = 3.5 * INCH_MM                 # actual 4x4
RAIL_THICKNESS_MM = 0.75 * INCH_MM      # actual 1x4 thickness
RAIL_WIDTH_MM = 3.5 * INCH_MM           # actual 1x4 width
METAL_THICKNESS_MM = 0.075 * INCH_MM
BRICK_LENGTH_MM = 16.0 * INCH_MM
BRICK_WIDTH_MM = 8.0 * INCH_MM
BRICK_HEIGHT_MM = 8.0 * INCH_MM


class AddOns(BaseModel):
    model_config = ConfigDict(extra="allow")

    top_rail: bool = True
    trellis: bool = False
    hardware_cloth: bool = False
    drainage_cloth: bool = False
    border_trim: bool = False
    show_soil: bool = True


class RaisedBedParams(BaseModel):
    model_config = ConfigDict(extra="allow")

    template_id: str | None = None
    template_name: str = "Raised Bed"
    length_ft: float = Field(gt=0, le=40)
    width_ft: float = Field(gt=0, le=20)
    height_ft: float = Field(gt=0, le=6)
    material: str = "wood"
    construction_style: str = "standard"
    addons: AddOns = Field(default_factory=AddOns)


@dataclass
class Component:
    name: str
    shape: cq.Workplane
    color: tuple[int, int, int]
    export: bool = True


@app.get("/")
def health() -> dict[str, Any]:
    return {
        "success": True,
        "service": "Raised Bed CAD Geometry Engine",
        "status": "running",
        "version": "3.0.0",
        "preview": "true-3d-software-rendered-png",
    }


@app.get("/health")
def health_alias() -> dict[str, Any]:
    return health()


@app.post("/preview-bed")
def preview_bed(params: RaisedBedParams) -> dict[str, Any]:
    try:
        normalized = normalize_params(params)
        components = build_components(normalized)
        png_bytes = render_3d_preview(components, normalized)
        preview_base64 = base64.b64encode(png_bytes).decode("ascii")

        return {
            "success": True,
            "preview_base64": preview_base64,
            "preview_data_url": f"data:image/png;base64,{preview_base64}",
            "summary": build_summary(normalized, components),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Preview generation failed: {exc}") from exc


@app.post("/generate-bed")
def generate_bed(params: RaisedBedParams) -> dict[str, Any]:
    try:
        normalized = normalize_params(params)
        components = build_components(normalized)

        with tempfile.TemporaryDirectory() as temp_dir:
            step_path = os.path.join(temp_dir, "raised_bed.step")
            stl_path = os.path.join(temp_dir, "raised_bed.stl")

            export_shape = make_export_compound(components)
            cq.exporters.export(export_shape, step_path)
            cq.exporters.export(export_shape, stl_path)

            step_base64 = encode_file(step_path)
            stl_base64 = encode_file(stl_path)

        png_bytes = render_3d_preview(components, normalized)
        preview_base64 = base64.b64encode(png_bytes).decode("ascii")

        return {
            "success": True,
            "step_base64": step_base64,
            "stl_base64": stl_base64,
            "preview_base64": preview_base64,
            "preview_data_url": f"data:image/png;base64,{preview_base64}",
            "summary": build_summary(normalized, components),
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"CAD generation failed: {exc}") from exc


def normalize_params(params: RaisedBedParams) -> RaisedBedParams:
    material = params.material.strip().lower()
    style = params.construction_style.strip().lower()

    if material not in {"wood", "metal", "brick"}:
        raise ValueError("material must be wood, metal, or brick")

    if style not in {"standard", "nailless"}:
        raise ValueError("construction_style must be standard or nailless")

    if material != "wood" and style == "nailless":
        style = "standard"

    data = params.model_dump()
    data["material"] = material
    data["construction_style"] = style
    return RaisedBedParams(**data)


def build_components(params: RaisedBedParams) -> list[Component]:
    if params.material == "wood":
        components = build_wood_components(params)
    elif params.material == "metal":
        components = build_metal_components(params)
    else:
        components = build_brick_components(params)

    components.extend(build_addon_components(params))
    return components


def box_shape(
    x_size: float,
    y_size: float,
    z_size: float,
    center_x: float,
    center_y: float,
    center_z: float,
) -> cq.Workplane:
    return (
        cq.Workplane("XY")
        .box(x_size, y_size, z_size)
        .translate((center_x, center_y, center_z))
    )


def build_wood_components(params: RaisedBedParams) -> list[Component]:
    length = params.length_ft * FOOT_MM
    width = params.width_ft * FOOT_MM
    height = params.height_ft * FOOT_MM

    t = WOOD_THICKNESS_MM
    post = POST_MM
    components: list[Component] = []

    courses = max(1, math.ceil(height / WOOD_BOARD_WIDTH_MM))

    for course in range(courses):
        z0 = course * WOOD_BOARD_WIDTH_MM
        course_height = min(WOOD_BOARD_WIDTH_MM, height - z0)
        z_center = z0 + course_height / 2.0

        if params.construction_style == "nailless":
            components.extend(
                build_nailless_wood_course(
                    length=length,
                    width=width,
                    thickness=t,
                    course_height=course_height,
                    z0=z0,
                    course_index=course,
                )
            )
        else:
            front = box_shape(length, t, course_height, 0, -width / 2 + t / 2, z_center)
            back = box_shape(length, t, course_height, 0, width / 2 - t / 2, z_center)
            left = box_shape(t, max(t, width - 2 * t), course_height, -length / 2 + t / 2, 0, z_center)
            right = box_shape(t, max(t, width - 2 * t), course_height, length / 2 - t / 2, 0, z_center)

            components.extend(
                [
                    Component(f"front_board_{course + 1}", front, (190, 128, 83)),
                    Component(f"back_board_{course + 1}", back, (178, 116, 75)),
                    Component(f"left_board_{course + 1}", left, (168, 103, 66)),
                    Component(f"right_board_{course + 1}", right, (160, 96, 62)),
                ]
            )

    if params.construction_style == "standard":
        post_positions = [
            (-length / 2 + post / 2, -width / 2 + post / 2),
            (length / 2 - post / 2, -width / 2 + post / 2),
            (-length / 2 + post / 2, width / 2 - post / 2),
            (length / 2 - post / 2, width / 2 - post / 2),
        ]
        for idx, (px, py) in enumerate(post_positions, start=1):
            post_shape = box_shape(post, post, height, px, py, height / 2)
            components.append(Component(f"corner_post_{idx}", post_shape, (135, 82, 53)))

    if params.addons.top_rail:
        rail_t = RAIL_THICKNESS_MM
        rail_w = RAIL_WIDTH_MM
        z = height + rail_t / 2

        components.extend(
            [
                Component(
                    "front_top_rail",
                    box_shape(length + rail_w, rail_w, rail_t, 0, -width / 2, z),
                    (144, 88, 57),
                ),
                Component(
                    "back_top_rail",
                    box_shape(length + rail_w, rail_w, rail_t, 0, width / 2, z),
                    (144, 88, 57),
                ),
                Component(
                    "left_top_rail",
                    box_shape(rail_w, max(rail_w, width - rail_w), rail_t, -length / 2, 0, z),
                    (126, 74, 48),
                ),
                Component(
                    "right_top_rail",
                    box_shape(rail_w, max(rail_w, width - rail_w), rail_t, length / 2, 0, z),
                    (126, 74, 48),
                ),
            ]
        )

    return components


def build_nailless_wood_course(
    length: float,
    width: float,
    thickness: float,
    course_height: float,
    z0: float,
    course_index: int,
) -> list[Component]:
    """Create complementary half-lap corner notches for one wood course."""
    z_center = z0 + course_height / 2.0
    half_height = course_height / 2.0
    clearance = 0.6

    front = box_shape(length, thickness, course_height, 0, -width / 2 + thickness / 2, z_center)
    back = box_shape(length, thickness, course_height, 0, width / 2 - thickness / 2, z_center)
    left = box_shape(thickness, width, course_height, -length / 2 + thickness / 2, 0, z_center)
    right = box_shape(thickness, width, course_height, length / 2 - thickness / 2, 0, z_center)

    # Long boards: remove the lower half at each corner.
    for x_pos in (-length / 2 + thickness / 2, length / 2 - thickness / 2):
        lower_front_cut = box_shape(
            thickness + clearance,
            thickness + clearance,
            half_height + clearance,
            x_pos,
            -width / 2 + thickness / 2,
            z0 + half_height / 2,
        )
        lower_back_cut = box_shape(
            thickness + clearance,
            thickness + clearance,
            half_height + clearance,
            x_pos,
            width / 2 - thickness / 2,
            z0 + half_height / 2,
        )
        front = front.cut(lower_front_cut)
        back = back.cut(lower_back_cut)

    # End boards: remove the upper half at each corner.
    for y_pos in (-width / 2 + thickness / 2, width / 2 - thickness / 2):
        upper_left_cut = box_shape(
            thickness + clearance,
            thickness + clearance,
            half_height + clearance,
            -length / 2 + thickness / 2,
            y_pos,
            z0 + half_height + half_height / 2,
        )
        upper_right_cut = box_shape(
            thickness + clearance,
            thickness + clearance,
            half_height + clearance,
            length / 2 - thickness / 2,
            y_pos,
            z0 + half_height + half_height / 2,
        )
        left = left.cut(upper_left_cut)
        right = right.cut(upper_right_cut)

    index = course_index + 1
    return [
        Component(f"nailless_front_board_{index}", front, (190, 128, 83)),
        Component(f"nailless_back_board_{index}", back, (178, 116, 75)),
        Component(f"nailless_left_board_{index}", left, (168, 103, 66)),
        Component(f"nailless_right_board_{index}", right, (160, 96, 62)),
    ]


def build_metal_components(params: RaisedBedParams) -> list[Component]:
    length = params.length_ft * FOOT_MM
    width = params.width_ft * FOOT_MM
    height = params.height_ft * FOOT_MM
    t = max(METAL_THICKNESS_MM, 1.5)

    components = [
        Component("front_panel", box_shape(length, t, height, 0, -width / 2 + t / 2, height / 2), (132, 145, 156)),
        Component("back_panel", box_shape(length, t, height, 0, width / 2 - t / 2, height / 2), (119, 133, 145)),
        Component("left_panel", box_shape(t, width, height, -length / 2 + t / 2, 0, height / 2), (108, 122, 134)),
        Component("right_panel", box_shape(t, width, height, length / 2 - t / 2, 0, height / 2), (101, 115, 127)),
    ]

    # Corrugation ribs are modeled as narrow 3D strips for visual realism.
    rib_spacing = 4.0 * INCH_MM
    rib_depth = 0.25 * INCH_MM
    x = -length / 2 + rib_spacing / 2
    rib_index = 1
    while x < length / 2:
        components.append(
            Component(
                f"front_rib_{rib_index}",
                box_shape(rib_depth, rib_depth, height, x, -width / 2 - rib_depth / 2, height / 2),
                (180, 190, 198),
            )
        )
        rib_index += 1
        x += rib_spacing

    return components


def build_brick_components(params: RaisedBedParams) -> list[Component]:
    length = params.length_ft * FOOT_MM
    width = params.width_ft * FOOT_MM
    height = params.height_ft * FOOT_MM

    courses = max(1, math.ceil(height / BRICK_HEIGHT_MM))
    components: list[Component] = []

    long_count = max(1, math.ceil(length / BRICK_LENGTH_MM))
    short_count = max(1, math.ceil(max(BRICK_LENGTH_MM, width - 2 * BRICK_WIDTH_MM) / BRICK_LENGTH_MM))

    for course in range(courses):
        z0 = course * BRICK_HEIGHT_MM
        course_height = min(BRICK_HEIGHT_MM, height - z0)
        z = z0 + course_height / 2
        offset = BRICK_LENGTH_MM / 2 if course % 2 else 0.0

        for i in range(long_count):
            cx = -length / 2 + BRICK_LENGTH_MM / 2 + i * BRICK_LENGTH_MM + offset
            while cx > length / 2:
                cx -= length
            if -length / 2 <= cx <= length / 2:
                components.append(
                    Component(
                        f"front_block_{course}_{i}",
                        box_shape(min(BRICK_LENGTH_MM, length), BRICK_WIDTH_MM, course_height, cx, -width / 2 + BRICK_WIDTH_MM / 2, z),
                        (170, 83, 63),
                    )
                )
                components.append(
                    Component(
                        f"back_block_{course}_{i}",
                        box_shape(min(BRICK_LENGTH_MM, length), BRICK_WIDTH_MM, course_height, cx, width / 2 - BRICK_WIDTH_MM / 2, z),
                        (151, 72, 56),
                    )
                )

        inner_width = max(BRICK_LENGTH_MM, width - 2 * BRICK_WIDTH_MM)
        for i in range(short_count):
            cy = -inner_width / 2 + BRICK_LENGTH_MM / 2 + i * BRICK_LENGTH_MM
            components.append(
                Component(
                    f"left_block_{course}_{i}",
                    box_shape(BRICK_WIDTH_MM, min(BRICK_LENGTH_MM, inner_width), course_height, -length / 2 + BRICK_WIDTH_MM / 2, cy, z),
                    (158, 76, 58),
                )
            )
            components.append(
                Component(
                    f"right_block_{course}_{i}",
                    box_shape(BRICK_WIDTH_MM, min(BRICK_LENGTH_MM, inner_width), course_height, length / 2 - BRICK_WIDTH_MM / 2, cy, z),
                    (142, 66, 51),
                )
            )

    return components


def build_addon_components(params: RaisedBedParams) -> list[Component]:
    length = params.length_ft * FOOT_MM
    width = params.width_ft * FOOT_MM
    height = params.height_ft * FOOT_MM
    components: list[Component] = []

    if params.addons.hardware_cloth:
        components.append(
            Component(
                "hardware_cloth",
                box_shape(max(1, length - 10), max(1, width - 10), 2.0, 0, 0, 2.0),
                (125, 134, 140),
            )
        )

    if params.addons.drainage_cloth:
        components.append(
            Component(
                "drainage_cloth",
                box_shape(max(1, length - 16), max(1, width - 16), 1.2, 0, 0, 5.0),
                (78, 96, 90),
            )
        )

    if params.addons.show_soil:
        wall_t = WOOD_THICKNESS_MM if params.material == "wood" else max(METAL_THICKNESS_MM, BRICK_WIDTH_MM if params.material == "brick" else METAL_THICKNESS_MM)
        inset = min(max(20.0, wall_t + 8.0), min(length, width) / 4.0)
        soil_height = max(10.0, height * 0.82)
        components.append(
            Component(
                "soil_preview",
                box_shape(max(1, length - 2 * inset), max(1, width - 2 * inset), soil_height, 0, 0, soil_height / 2 + 6.0),
                (92, 65, 45),
                export=False,
            )
        )

    if params.addons.trellis:
        post_size = 1.0 * INCH_MM
        trellis_height = max(5.0 * FOOT_MM, height + 3.0 * FOOT_MM)
        back_y = width / 2 + post_size / 2
        x_left = -length / 2 + post_size
        x_right = length / 2 - post_size

        components.extend(
            [
                Component("trellis_post_left", box_shape(post_size, post_size, trellis_height, x_left, back_y, trellis_height / 2), (82, 94, 104)),
                Component("trellis_post_right", box_shape(post_size, post_size, trellis_height, x_right, back_y, trellis_height / 2), (82, 94, 104)),
            ]
        )

        rail_count = 5
        for idx in range(rail_count):
            z = height + (idx + 1) * (trellis_height - height) / (rail_count + 1)
            components.append(
                Component(
                    f"trellis_rail_{idx + 1}",
                    box_shape(max(post_size, length - 2 * post_size), post_size / 2, post_size / 2, 0, back_y, z),
                    (115, 126, 134),
                )
            )

    return components


def make_export_compound(components: list[Component]) -> cq.Shape:
    shapes = [component.shape.val() for component in components if component.export]
    if not shapes:
        raise ValueError("No exportable geometry was created")
    return cq.Compound.makeCompound(shapes)


def encode_file(path: str) -> str:
    with open(path, "rb") as handle:
        return base64.b64encode(handle.read()).decode("ascii")


def build_summary(params: RaisedBedParams, components: list[Component]) -> dict[str, Any]:
    volume_cuft = params.length_ft * params.width_ft * params.height_ft
    return {
        "template_name": params.template_name,
        "length_ft": params.length_ft,
        "width_ft": params.width_ft,
        "height_ft": params.height_ft,
        "material": params.material,
        "construction_style": params.construction_style,
        "soil_volume_cuft": round(volume_cuft, 2),
        "soil_bags_1_5_cuft": math.ceil(volume_cuft / 1.5),
        "base_area_sqft": round(params.length_ft * params.width_ft, 2),
        "perimeter_ft": round(2 * (params.length_ft + params.width_ft), 2),
        "component_count": len([component for component in components if component.export]),
        "preview_renderer": "cadquery tessellation + Pillow software 3D renderer",
    }


def render_3d_preview(
    components: list[Component],
    params: RaisedBedParams,
    width: int = 1000,
    height: int = 700,
) -> bytes:
    """
    Render actual tessellated CAD geometry to PNG using a software painter's algorithm.
    No OpenGL, browser, GPU, EGL, or desktop display server is required.
    """
    supersample = 2
    canvas_w = width * supersample
    canvas_h = height * supersample

    image = Image.new("RGB", (canvas_w, canvas_h), (240, 245, 248))
    draw = ImageDraw.Draw(image, "RGBA")

    triangles: list[dict[str, Any]] = []
    all_points: list[tuple[float, float, float]] = []

    for component in components:
        shape = component.shape.val()
        vertices, faces = shape.tessellate(2.5, 0.25)
        vertex_xyz = [(float(v.x), float(v.y), float(v.z)) for v in vertices]
        all_points.extend(vertex_xyz)

        for face in faces:
            a = vertex_xyz[int(face[0])]
            b = vertex_xyz[int(face[1])]
            c = vertex_xyz[int(face[2])]
            triangles.append(
                {
                    "points": (a, b, c),
                    "base_color": component.color,
                }
            )

    if not all_points or not triangles:
        raise ValueError("The model contains no renderable geometry")

    min_x = min(point[0] for point in all_points)
    max_x = max(point[0] for point in all_points)
    min_y = min(point[1] for point in all_points)
    max_y = max(point[1] for point in all_points)
    min_z = min(point[2] for point in all_points)
    max_z = max(point[2] for point in all_points)

    center = (
        (min_x + max_x) / 2.0,
        (min_y + max_y) / 2.0,
        (min_z + max_z) / 2.0,
    )

    yaw = math.radians(-38.0)
    pitch = math.radians(28.0)

    def rotate(point: tuple[float, float, float]) -> tuple[float, float, float]:
        x = point[0] - center[0]
        y = point[1] - center[1]
        z = point[2] - center[2]

        x1 = x * math.cos(yaw) - y * math.sin(yaw)
        y1 = x * math.sin(yaw) + y * math.cos(yaw)
        z1 = z

        y2 = y1 * math.cos(pitch) - z1 * math.sin(pitch)
        z2 = y1 * math.sin(pitch) + z1 * math.cos(pitch)
        return x1, y2, z2

    rotated_points = [rotate(point) for point in all_points]
    proj_min_x = min(point[0] for point in rotated_points)
    proj_max_x = max(point[0] for point in rotated_points)
    proj_min_y = min(point[1] for point in rotated_points)
    proj_max_y = max(point[1] for point in rotated_points)

    usable_w = canvas_w * 0.82
    usable_h = canvas_h * 0.70
    scale_x = usable_w / max(1.0, proj_max_x - proj_min_x)
    scale_y = usable_h / max(1.0, proj_max_y - proj_min_y)
    scale = min(scale_x, scale_y)

    screen_center_x = canvas_w * 0.50
    screen_center_y = canvas_h * 0.57

    def project(point: tuple[float, float, float]) -> tuple[float, float, float]:
        x, y, depth = rotate(point)
        return (
            screen_center_x + x * scale,
            screen_center_y - y * scale,
            depth,
        )

    # Soft ground shadow.
    shadow_w = min(canvas_w * 0.58, (proj_max_x - proj_min_x) * scale * 1.05)
    shadow_h = max(24.0, shadow_w * 0.10)
    draw.ellipse(
        (
            screen_center_x - shadow_w / 2,
            canvas_h * 0.78 - shadow_h / 2,
            screen_center_x + shadow_w / 2,
            canvas_h * 0.78 + shadow_h / 2,
        ),
        fill=(0, 0, 0, 35),
    )

    rendered_triangles: list[dict[str, Any]] = []
    light = normalize_vector((-0.4, -0.65, 0.75))

    for triangle in triangles:
        p0, p1, p2 = triangle["points"]
        s0 = project(p0)
        s1 = project(p1)
        s2 = project(p2)

        normal = triangle_normal(p0, p1, p2)
        normal_rotated = rotate_vector(normal, yaw, pitch)
        normal_rotated = normalize_vector(normal_rotated)
        brightness = 0.48 + 0.52 * max(0.0, dot(normal_rotated, light))

        base = triangle["base_color"]
        fill = tuple(max(0, min(255, int(channel * brightness))) for channel in base)

        rendered_triangles.append(
            {
                "depth": (s0[2] + s1[2] + s2[2]) / 3.0,
                "points": [(s0[0], s0[1]), (s1[0], s1[1]), (s2[0], s2[1])],
                "fill": fill,
            }
        )

    rendered_triangles.sort(key=lambda item: item["depth"])

    for triangle in rendered_triangles:
        points = triangle["points"]
        fill = triangle["fill"]
        edge = tuple(max(0, int(channel * 0.62)) for channel in fill)
        draw.polygon(points, fill=(*fill, 255))
        draw.line([*points, points[0]], fill=(*edge, 90), width=1 * supersample)

    font_large = load_font(34 * supersample, bold=True)
    font_small = load_font(20 * supersample, bold=False)
    font_badge = load_font(18 * supersample, bold=True)

    title = params.template_name or "Raised Bed"
    subtitle = (
        f"{params.width_ft:g}' × {params.length_ft:g}' × {params.height_ft:g}'"
        f"   •   {params.material.title()}"
        f"   •   {('Nailless interlocking' if params.construction_style == 'nailless' else 'Standard hardware')}"
    )

    draw.text((48 * supersample, 34 * supersample), title, fill=(44, 54, 63, 255), font=font_large)
    draw.text((50 * supersample, 84 * supersample), subtitle, fill=(99, 112, 122, 255), font=font_small)

    badge_text = f"TRUE 3D • {len([c for c in components if c.export])} COMPONENTS"
    badge_box = draw.textbbox((0, 0), badge_text, font=font_badge)
    badge_w = badge_box[2] - badge_box[0] + 28 * supersample
    badge_h = badge_box[3] - badge_box[1] + 18 * supersample
    badge_x = canvas_w - badge_w - 38 * supersample
    badge_y = 38 * supersample
    draw.rounded_rectangle(
        (badge_x, badge_y, badge_x + badge_w, badge_y + badge_h),
        radius=14 * supersample,
        fill=(74, 93, 78, 232),
    )
    draw.text(
        (badge_x + 14 * supersample, badge_y + 6 * supersample),
        badge_text,
        fill=(255, 255, 255, 255),
        font=font_badge,
    )

    image = image.resize((width, height), Image.Resampling.LANCZOS)
    output = io.BytesIO()
    image.save(output, format="PNG", optimize=True)
    return output.getvalue()


def load_font(size: int, bold: bool) -> ImageFont.ImageFont:
    candidates = (
        ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"]
        if bold
        else ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]
    )
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size=size)
    return ImageFont.load_default()


def triangle_normal(
    a: tuple[float, float, float],
    b: tuple[float, float, float],
    c: tuple[float, float, float],
) -> tuple[float, float, float]:
    ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
    return (
        ab[1] * ac[2] - ab[2] * ac[1],
        ab[2] * ac[0] - ab[0] * ac[2],
        ab[0] * ac[1] - ab[1] * ac[0],
    )


def rotate_vector(
    vector: tuple[float, float, float],
    yaw: float,
    pitch: float,
) -> tuple[float, float, float]:
    x, y, z = vector
    x1 = x * math.cos(yaw) - y * math.sin(yaw)
    y1 = x * math.sin(yaw) + y * math.cos(yaw)
    z1 = z
    y2 = y1 * math.cos(pitch) - z1 * math.sin(pitch)
    z2 = y1 * math.sin(pitch) + z1 * math.cos(pitch)
    return x1, y2, z2


def normalize_vector(vector: tuple[float, float, float]) -> tuple[float, float, float]:
    length = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    if length == 0:
        return 0.0, 0.0, 1.0
    return vector[0] / length, vector[1] / length, vector[2] / length


def dot(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
