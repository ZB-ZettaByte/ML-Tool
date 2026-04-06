from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class AnnotationType(str, Enum):
    CLASSIFICATION = "classification"
    BOUNDING_BOX = "bounding_box"
    POLYGON = "polygon"

class BoundingBox(BaseModel):
    x: float = Field(
        ...,
        description = "X coordinate of the top-left corner of the bounding box",
    )
    y: float = Field(
        ...,
        description = "Y coordinate of the top-left corner of the bounding box",
    )
    width: float = Field(
        ...,
        description = "Width of the bounding box",
        gt = 0.0,
    )
    height: float = Field(
        ...,
        description = "Height of the bounding box",
        gt = 0.0,
    )
    label: str = Field(
        ...,
        description = "Label for the bounding box",
    )
    confidence: Optional[float] = Field(
        None,
        description = "Confidence score for the annotation",
        ge = 0.0,
        le = 1.0,
    )

class Polygon(BaseModel):
    points: List[float] = Field(
        ...,
        description = "List of x,y coordinates forming the polygon",
        min_length = 6,
    )
    label: str = Field(
        ...,
        description = "Label for the polygon",
        min_length = 1,
    )
    confidence: Optional[float] = Field (
        None, 
        ge = 0.0,
        le = 1.0,
        description = "Confidence score for the annotation",
    )

class Classification(BaseModel):
    label: str = Field(
        ...,
        description = "Class label for the entire image",
        min_length = 1,
    )
    confidence: Optional[float] = Field(
        None,
        ge = 0.0,
        le = 1.0,
        description = "Confidence score for the classification",
    )
    tags: Optional[List[str]] = Field(
        None,
        description = "Optional tags for additional metadata"
    )

class Annotation(BaseModel):
    id: Optional[str] = Field(
        None, 
        description = "Unique identifier for the annotation"
    )
    image_id: str = Field(
        ...,
        description = "ID of the image being annotated",
    )
    type: AnnotationType = Field(
        ...,
        description = "Type of annotation (classification, bounding_box, polygon)",
    )
    bounding_box: Optional[BoundingBox] = Field (
        None,
        description = "Bounding box annotation",
    )
    polygon : Optional[Polygon] = Field(
        None, 
        description = "Polygon annotation",
    )
    classification : Optional[Classification] = Field (
        None,
        description = "Classfication annotation",
    )
    created_at: Optional[str] = Field(
        None,
        description = "Timestamp when the annotation was created",
    )