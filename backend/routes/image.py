import re
from typing import List
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from backend.services.azure_storage import upload_image as azure_upload
from backend.services.azure_storage import upload_image as azure_upload, delete_image as azure_delete
from backend.services.azure_storage import upload_image as azure_upload, delete_image as azure_delete, list_images as azure_list

router = APIRouter(
    prefix = "/images",
    tags = ["images"],
    responses = {
        404: {"description": "Not found"},
        400: {"description": "Bad request"},
    },
)

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
MAX_FILE_SIZE = 10 * 1024 * 1024

@router.post(
    "/upload",
    responses={
        400: {"description": "Bad request - invalid file type or size"},
        200: {"description": "Image uploaded successfully"},
    }
)

async def upload_image(file: UploadFile = File(...)):
    #Validate file types
    extension = file.filename.split(".")[-1].lower() # type: ignore
    if extension not in ALLOWED_EXTENSIONS:
        return JSONResponse(
            status_code = 400,
            content = {
                "detail": f"Invalid file type. Allowed types: {', '.join(ALLOWED_EXTENSIONS)}"
            }
        )
    # Validate file size
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        return JSONResponse(
            status_code=400,
            content = {
                "detail": f"File size exceeds the maximum limit of {MAX_FILE_SIZE // (1024 * 1024)}MB"
            }
        )

    filename = file.filename or "unknown.jpg"
    filename = re.sub(r'\s+', '_', filename)
    url = await azure_upload(contents, str(filename))

    return JSONResponse(
        status_code = 200,
        content = {
            "filename": file.filename,
            "size": len(contents),
            "extension": extension,
            "url": url,
            "message": "Image uploaded successfully",
        }
    )

@router.delete(
    "/delete/{filename}",
    responses={
        200: {"description": "Image deleted successfully"},
        400: {"description": "Bad request - deletion failed"},
    }
)

async def delete_image(filename: str):
    try:
        await azure_delete(filename)
        return JSONResponse(
            status_code = 200,
            content = {"message": "Image deleted successfully"},
        )
    except ValueError as e:
        return JSONResponse(
            status_code = 400,
            content = {"detail": str(e)},
        )

@router.get(
    "/list",
    responses={
        200: {"description": "List of images retrieved successfully"},
        400: {"description": "Bad request - failed to retrieve images"},
    }
)

async def list_images():
    try:
        images = await azure_list()
        return JSONResponse(
            status_code = 200,
            content = {
                "images": images,
                "total": len(images),
                "message": f"Found {len(images)} images"
            }
        )
    except ValueError as e:
        return JSONResponse(
            status_code = 400,
            content = {"detail": str(e)},
        )