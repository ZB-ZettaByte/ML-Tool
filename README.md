# ML Data Annotation Tool

![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

> **Note:** This project is currently under active development. Features may be incomplete or subject to change.

A full-stack web application for annotating machine learning datasets with support for **bounding boxes**, **polygons**, and **image classification**. Images are stored on **Azure Blob Storage** and annotations are persisted locally as JSON.

---

## Features

- **Three annotation types** — bounding box, polygon, and classification
- **Image management** — upload, list, and delete images via Azure Blob Storage
- **Annotation storage** — save and retrieve annotations per image as JSON
- **Input validation** — confidence scores, label checks, polygon point validation
- **Interactive dashboard** — charts, data tables, and section cards
- **Particle canvas** landing page with animated hero section
- **REST API** with auto-generated Swagger docs

---

## Tech Stack

| Layer    | Technology                                      |
|----------|-------------------------------------------------|
| Frontend | Next.js 16, React, Tailwind CSS, shadcn/ui      |
| Backend  | FastAPI, Python, Pydantic v2, Uvicorn           |
| Storage  | Azure Blob Storage (images), JSON files (annotations) |

---

## Project Structure

```
ML-Data-Annotation-Tool/
├── backend/
│   ├── main.py                  # FastAPI app, CORS, router registration
│   ├── models.py                # Pydantic models (Annotation, BoundingBox, Polygon, Classification)
│   ├── routes/
│   │   ├── image.py             # POST /images/upload, DELETE /images/delete, GET /images/list
│   │   └── annotations.py      # POST /annotations/save, GET /annotations/get/{image_id}
│   ├── services/
│   │   └── azure_storage.py    # Azure Blob Storage client (upload, delete, list)
│   └── validators/
│       └── validator.py        # Annotation validation logic
├── frontend/
│   ├── app/
│   │   ├── page.tsx            # Landing page (Hero section)
│   │   ├── layout.tsx          # Root layout
│   │   ├── globals.css
│   │   └── dashboard/
│   │       ├── page.tsx        # Dashboard page
│   │       └── data.json       # Dashboard seed data
│   ├── components/
│   │   ├── hero-section.tsx
│   │   ├── particle-canvas.tsx
│   │   ├── header.tsx
│   │   ├── app-sidebar.tsx
│   │   ├── data-table.tsx
│   │   ├── chart-area-interactive.tsx
│   │   └── ui/                 # shadcn/ui components
│   └── hooks/
│       └── use-mobile.ts
├── annotations_data/           # Per-image annotation JSON files
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+
- Azure Storage account (for image upload/delete/list)

### 1. Clone the repo

```bash
git clone <repo-url>
cd ML-Data-Annotation-Tool
```

### 2. Backend setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
AZURE_STORAGE_CONNECTION_STRING=your_connection_string_here
AZURE_CONTAINER_NAME=your_container_name_here
```

Start the API server:

```bash
uvicorn backend.main:app --reload
```

- API: `http://localhost:8000`
- Swagger docs: `http://localhost:8000/docs`

### 3. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

- App: `http://localhost:3000`

---

## API Reference

### General

| Method | Endpoint           | Description       |
|--------|--------------------|-------------------|
| GET    | `/`                | API status        |
| GET    | `/health`          | Health check      |

### Images

| Method | Endpoint                    | Description                              |
|--------|-----------------------------|------------------------------------------|
| POST   | `/images/upload`            | Upload an image (jpg, jpeg, png, webp, max 10MB) |
| DELETE | `/images/delete/{filename}` | Delete an image from Azure              |
| GET    | `/images/list`              | List all images in Azure container      |

### Annotations

| Method | Endpoint                          | Description                         |
|--------|-----------------------------------|-------------------------------------|
| POST   | `/annotations/save`               | Save an annotation for an image     |
| GET    | `/annotations/get/{image_id}`     | Get all annotations for an image    |

---

## Annotation Types

### Bounding Box
```json
{
  "image_id": "img_001",
  "type": "bounding_box",
  "bounding_box": {
    "x": 10.0,
    "y": 20.0,
    "width": 100.0,
    "height": 50.0,
    "label": "cat",
    "confidence": 0.95
  }
}
```

### Polygon
```json
{
  "image_id": "img_001",
  "type": "polygon",
  "polygon": {
    "points": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
    "label": "road",
    "confidence": 0.88
  }
}
```

### Classification
```json
{
  "image_id": "img_001",
  "type": "classification",
  "classification": {
    "label": "outdoor",
    "confidence": 0.99,
    "tags": ["nature", "daytime"]
  }
}
```