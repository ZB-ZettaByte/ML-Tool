import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()

AZURE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
AZURE_CONTAINER_NAME = os.getenv("AZURE_CONTAINER_NAME", "")

def get_blob_service_client():
    if not AZURE_CONNECTION_STRING:
        raise ValueError(
            "AZURE_STORAGE_CONNECTION_STRING is not set in .env file"
        )
    return BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)

async def upload_image(file_contents: bytes, filename: str) -> str:
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(
            container = AZURE_CONTAINER_NAME,
            blob = filename,
        )
        blob_client.upload_blob(
            file_contents,
            overwrite = True,
        ) 
        return blob_client.url

    except Exception as e:
        raise ValueError(f"Failed to upload image to Azure Blob Storage: {str(e)}")

async def delete_image(filename: str) -> bool:
    try:
        client = get_blob_service_client()
        blob_client = client.get_blob_client(
            container = AZURE_CONTAINER_NAME,
            blob = filename,
        )
        blob_client.delete_blob()
        return True
    except Exception as e:
        raise ValueError(f"Failed to delete image from Azure Blob Storage: {str(e)}")
    
async def list_images() -> list:
    try:
        client = get_blob_service_client()
        container_client = client.get_container_client(AZURE_CONTAINER_NAME)
        blobs = container_client.list_blobs()
        return [{"filename": blob.name, "size": blob.size} for blob in blobs]
    except Exception as e:
        raise ValueError(f"Failed to list images from Azure Blob Storage: {str(e)}")