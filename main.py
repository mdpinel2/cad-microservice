from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from cadquery import exporters
import cadquery as cq
import base64
import tempfile
import os
import io
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Text-to-CAD Geometry Engine")

# Enable CORS for Google Apps Script communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class BracketParams(BaseModel):
    length: float = 50
    height: float = 50
    width: float = 30
    thickness: float = 3
    hole_dia: float = 5
    template_name: Optional[str] = "L-Bracket"

def create_bracket(params: BracketParams):
    pts = [
        (0, 0), (params.length, 0), (params.length, params.thickness),
        (params.thickness, params.thickness), (params.thickness, params.height), (0, params.height)
    ]
    bracket = cq.Workplane("front").polyline(pts).close().extrude(params.width)
    fillet_radius = min(1.5, params.thickness / 3)
    if fillet_radius > 0:
        bracket = bracket.edges("|Z").fillet(fillet_radius)
    bracket = bracket.faces("<Y").workplane(centerOption="CenterOfMass").center(params.length / 4, 0).hole(params.hole_dia)
    bracket = bracket.faces("<X").workplane(centerOption="CenterOfMass").center(params.height / 4, 0).hole(params.hole_dia)
    return bracket

@app.post("/generate-bracket")
def generate_bracket_api(params: BracketParams):
    bracket = create_bracket(params)
    step_path = tempfile.mktemp(suffix=".step")
    stl_path = tempfile.mktemp(suffix=".stl")
    
    cq.exporters.export(bracket, step_path)
    cq.exporters.export(bracket, stl_path)
    
    with open(step_path, "rb") as f: step_b64 = base64.b64encode(f.read()).decode("utf-8")
    with open(stl_path, "rb") as f: stl_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    os.remove(step_path)
    os.remove(stl_path)
    return {"success": True, "step_base64": step_b64, "stl_base64": stl_b64}

@app.post("/preview-bracket")
def preview_bracket(params: BracketParams):
    bracket = create_bracket(params)
    img_path = tempfile.mktemp(suffix=".png")
    
    try:
        exporters.export(bracket, img_path, exporters.ExportTypes.PNG, opt={
            'width': 420, 
            'height': 280, 
            'renderMode': 'shaded',
            'quality': 90
        })
        with open(img_path, "rb") as f:
            b64_img = base64.b64encode(f.read()).decode("utf-8")
        return {"success": True, "thumbnail_base64": b64_img}
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)
