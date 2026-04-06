from backend.models import Annotation, AnnotationType
from typing import List

def validate_annotation(annotation: Annotation) -> dict:
    errors = []
    warnings = []

    if annotation.type == AnnotationType.BOUNDING_BOX:
        if annotation.bounding_box is None:
            errors.append("Bounding box data is missing for bounding box type")

    if annotation.type == AnnotationType.POLYGON:
        if annotation.polygon is None:
            errors.append("Polygon data is missing for polygon type")

    if annotation.type == AnnotationType.CLASSIFICATION:
        if annotation.classification is None:
            errors.append("Classification data is missing for classification type")
    
    if annotation.bounding_box and annotation.bounding_box.confidence is None:
        warnings.append("Confidence score is missing for bounding box")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }

def validate_dataset(annotations: List[Annotation]) -> dict:
    errors = []
    warnings = []

    image_ids = []
    for annotation in annotations:
        image_ids.append(annotation.image_id)
    
    duplicate_ids = []
    for image_id in image_ids:
        if image_ids.count(image_id) > 1:
            if image_id not in duplicate_ids:
                duplicate_ids.append(image_id)

    if len(duplicate_ids) > 0:
        errors.append(f"Duplicate image IDs found: {', '.join(duplicate_ids)}")
    
    for annotation in annotations:
        result = validate_annotation(annotation)
        if not result["valid"]:
            errors.extend(result["errors"])
        warnings.extend(result["warnings"])
    
    types_used = []
    for annotation in annotations:
        if annotation.type not in types_used:
            types_used.append(annotation.type)
    
    if len(types_used) > 1:
        warnings.append(f"Multiple annotation types found: {types_used}")
    
    return {
        "valid": len(errors) == 0,
        "total_annotations": len(annotations),
        "errors": errors,
        "warnings": warnings,
        "error_rate": round(len(errors) / max(len(annotations), 1) * 100, 2),
    }