from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
from PIL import Image, ImageDraw

import base64
import cadquery as cq
import io
import math
import os
import tempfile


app = FastAPI(title="Raised Bed CAD Geometry Engine")


class AddOns(BaseModel):
    trellis: bool = False
    hardware_cloth: bool = False
    drainage_cloth: bool = False
    border_trim: bool = False


class RaisedBedParams(BaseModel):
    template_id: str = "custom"
    template_name: str = "Custom Raised Bed"
    length_ft: float = Field(gt=0, le=30)
    width_ft: float = Field(gt=0, le=20)
    height_ft: float = Field(gt=0, le=6)
    material: str = "wood"
    construction_style: str = "standard"
    addons: AddOns = AddOns()


MM_PER_INCH = 25.4
INCHES_PER_FOOT = 12.0


def feet_to_mm(feet: float) -> float:
    return feet * INCHES_PER_FOOT * MM_PER_INCH


def wall_thickness_mm(material: str) -> float:
    values = {
        "wood": 1.5 * MM_PER_INCH,
        "metal": 0.075 * MM_PER_INCH,
        "brick": 8.0 * MM_PER_INCH,
    }
    return values.get(material, 1.5 * MM_PER_INCH)


def validate_material(material: str) -> None:
    if material not in {"wood", "metal", "brick"}:
        raise HTTPException(status_code=400, detail="Material must be wood, metal, or brick.")


def create_raised_bed(params: RaisedBedParams):
    validate_material(params.material)

    length = feet_to_mm(params.length_ft)
    width = feet_to_mm(params.width_ft)
    height = feet_to_mm(params.height_ft)
    wall = wall_thickness_mm(params.material)

    max_wall = min(length, width) * 0.45
    wall = min(wall, max_wall)

    outer = (
        cq.Workplane("XY")
        .box(length, width, height, centered=(True, True, False))
    )

    inner_length = length - (2 * wall)
    inner_width = width - (2 * wall)

    if inner_length <= 0 or inner_width <= 0:
        raise HTTPException(status_code=400, detail="Dimensions are too small for the selected material.")

    inner = (
        cq.Workplane("XY")
        .box(inner_length, inner_width, height + 2, centered=(True, True, False))
        .translate((0, 0, 1))
    )

    bed = outer.cut(inner)

    if params.material == "wood":
        corner_post = min(3.5 * MM_PER_INCH, max_wall)
        post = cq.Workplane("XY").box(
            corner_post,
            corner_post,
            height,
            centered=(True, True, False)
        )

        x = (length / 2) - (corner_post / 2)
        y = (width / 2) - (corner_post / 2)

        for px in (-x, x):
            for py in (-y, y):
                bed = bed.union(post.translate((px, py, 0)))

    return bed


def build_summary(params: RaisedBedParams) -> Dict:
    soil_volume = params.length_ft * params.width_ft * params.height_ft
    base_area = params.length_ft * params.width_ft
    perimeter = 2 * (params.length_ft + params.width_ft)

    return {
        "soil_volume_cu_ft": round(soil_volume, 2),
        "soil_bags_1_5_cu_ft": math.ceil(soil_volume / 1.5),
        "base_area_sq_ft": round(base_area, 2),
        "perimeter_linear_ft": round(perimeter, 2),
    }


def make_preview_thumbnail(params: RaisedBedParams) -> str:
    image = Image.new("RGB", (700, 460), "#f5f7f9")
    draw = ImageDraw.Draw(image)

    material_colors = {
        "wood": "#B17852",
        "metal": "#77838F",
        "brick": "#A84F3E",
    }

    color = material_colors.get(params.material, "#B17852")

    max_dim = max(params.length_ft, params.width_ft, 1)
    long_px = int(230 + min(180, (params.length_ft / max_dim) * 170))
    side_px = int(85 + min(90, (params.width_ft / max_dim) * 85))
    height_px = int(50 + min(150, params.height_ft * 48))

    x = 90
    y = 280
    slant = int(side_px * 0.45)

    front = [
        (x, y),
        (x + long_px, y),
        (x + long_px, y + height_px),
        (x, y + height_px),
    ]

    left = [
        (x, y),
        (x + side_px, y - slant),
        (x + side_px, y - slant + height_px),
        (x, y + height_px),
    ]

    right = [
        (x + long_px, y),
        (x + long_px + side_px, y - slant),
        (x + long_px + side_px, y - slant + height_px),
        (x + long_px, y + height_px),
    ]

    top = [
        (x, y),
        (x + long_px, y),
        (x + long_px + side_px, y - slant),
        (x + side_px, y - slant),
    ]

    draw.polygon(left, fill=color, outline="#3a3a3a")
    draw.polygon(front, fill=color, outline="#3a3a3a")
    draw.polygon(right, fill=color, outline="#3a3a3a")
    draw.polygon(top, fill="#302a22", outline="#3a3a3a")

    inset = 12
    inner = [
        (x + inset, y - 4),
        (x + long_px - inset, y - 4),
        (x + long_px + side_px - inset, y - slant + inset),
        (x + side_px + inset, y - slant + inset),
    ]
    draw.polygon(inner, fill="#624a34")

    draw.text((28, 24), params.template_name, fill="#20262d")
    draw.text(
        (28, 54),
        f"{params.width_ft:g}' x {params.length_ft:g}' x {params.height_ft:g}'  |  {params.material.title()}",
        fill="#5d6670",
    )

    buffer = io.BytesIO()
    image.save(buffer, format="PNG", optimize=True)

    return base64.b64encode(buffer.getvalue()).decode("utf-8")


@app.get("/")
def health_check():
    return {
        "success": True,
        "service": "Raised Bed CAD Geometry Engine",
        "status": "running",
    }


@app.post("/preview-bed")
def preview_bed(params: RaisedBedParams):
    return {
        "success": True,
        "thumbnail_base64": make_preview_thumbnail(params),
        "summary": build_summary(params),
    }


@app.post("/generate-bed")
def generate_bed(params: RaisedBedParams):
    step_path = None
    stl_path = None

    try:
        bed = create_raised_bed(params)

        with tempfile.NamedTemporaryFile(suffix=".step", delete=False) as step_file:
            step_path = step_file.name

        with tempfile.NamedTemporaryFile(suffix=".stl", delete=False) as stl_file:
            stl_path = stl_file.name

        cq.exporters.export(bed, step_path)
        cq.exporters.export(bed, stl_path)

        with open(step_path, "rb") as file:
            step_b64 = base64.b64encode(file.read()).decode("utf-8")

        with open(stl_path, "rb") as file:
            stl_b64 = base64.b64encode(file.read()).decode("utf-8")

        return {
            "success": True,
            "step_base64": step_b64,
            "stl_base64": stl_b64,
            "summary": build_summary(params),
        }

    except HTTPException:
        raise

    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    finally:
        if step_path and os.path.exists(step_path):
            os.remove(step_path)

        if stl_path and os.path.exists(stl_path):
            os.remove(stl_path)
