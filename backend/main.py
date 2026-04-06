import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.models import Annotation, AnnotationType
from backend.routes.image import router as image_router
from backend.routes.annotations import router as annotations_router

app = FastAPI(
    title = "ML Annotation Tool API",
    version = "1.0.0",
    description = "API for annotating and managing ML datasets",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_router)
app.include_router(annotations_router)

@app.get("/")
async def root():
    return {"message": "ML Annotation tool API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.post("/test-annotation")
async def test_annotation(annotation: Annotation):
    return {
        "message": "Annotation received successfully",
        "annotation": annotation,
    }