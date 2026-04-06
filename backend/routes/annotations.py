import json
import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.models import Annotation, AnnotationType
from backend.validators.validator import validate_annotation
from datetime import datetime

router = APIRouter(
    prefix = "/annotations",
    tags = ["annotations"],
    responses = {
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
    },
)

ANNOTATIONS_DIR = "annotations_data"

def ensure_annotations_dir():
    if not os.path.exists(ANNOTATIONS_DIR):
        os.makedirs(ANNOTATIONS_DIR)

@router.post("/save")
async def save_annotation(annotation: Annotation):
    try:
        validation = validate_annotation(annotation)

        if not validation["valid"]:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message": "Annotation validation failed",
                    "errors": validation["errors"],
                    "warnings": validation["warnings"],
                }
            )

        ensure_annotations_dir()

        annotation_dic = annotation.model_dump()
        annotation_dic["created_at"] = datetime.utcnow().isoformat()

        filename = f"{annotation.image_id}.json"
        filepath = os.path.join(ANNOTATIONS_DIR, filename)

        existing = []
        if os.path.exists(filepath):
            with open(filepath, "r") as f:
                existing = json.load(f)
        
        existing.append(annotation_dic)
        
        with open(filepath, "w") as f:
            json.dump(existing, f, indent=2)

        return JSONResponse(
            status_code = 200,
            content = {
                "message": "Annotation saved successfully",
                "image_id": annotation.image_id,
                "total_annotations": len(existing),
                "warnings": validation["warnings"],
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code = 400,
            content = {
                "detail": str(e)
            }
        )

@router.get("/get/{image_id}")
async def get_annotations(image_id: str):
    try:
        filepath = os.path.join(ANNOTATIONS_DIR, f"{image_id}.json")

        if not os.path.exists(filepath):
            return JSONResponse(
                status_code = 404,
                content = {
                    "image_id": image_id,
                    "annotations": [],
                    "total": 0,
                    "message": "No annotations found for this image"
                }
            )
        
        with open(filepath, "r") as f:
            annotations = json.load(f)
        return JSONResponse(
            status_code = 200, 
            content = { 
                "image_id": image_id, 
                "annotations": annotations, 
                "total": len(annotations),
                "message": f"Found {len(annotations)} annotations"
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code = 400, 
            content = {
                "detail": str(e)
            }
        )