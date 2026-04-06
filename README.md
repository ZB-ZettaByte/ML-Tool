# ML Data Annotation Tool

A full-stack web application for annotating and managing machine learning datasets. Built with a **Next.js** frontend and a **FastAPI** backend.

---

## Features

- Image upload and management
- Annotation creation and storage (bounding boxes, labels, etc.)
- Interactive dashboard with charts and data tables
- Particle canvas landing page
- REST API for programmatic access

---

## Tech Stack

| Layer    | Technology                        |
|----------|-----------------------------------|
| Frontend | Next.js 15, React, Tailwind CSS   |
| Backend  | FastAPI, Python, Pydantic, Uvicorn|
| Storage  | Local filesystem / JSON           |

---

## Project Structure

```
ML-Data-Annotation-Tool/
├── backend/
│   ├── main.py            # FastAPI app entry point
│   ├── models.py          # Pydantic data models
│   ├── routes/
│   │   ├── image.py       # Image upload/retrieval routes
│   │   └── annotations.py # Annotation CRUD routes
│   ├── services/          # Business logic
│   └── validators/        # Input validation
├── frontend/
│   ├── app/
│   │   ├── dashboard/     # Dashboard page
│   │   └── globals.css
│   ├── components/        # Reusable UI components
│   └── hooks/             # Custom React hooks
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- Node.js 18+

### Backend

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the API server
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`.  
Interactive docs: `http://localhost:8000/docs`

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:3000`.

---

## API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| GET    | `/`                 | API status               |
| GET    | `/health`           | Health check             |
| POST   | `/test-annotation`  | Test annotation payload  |
| *      | `/images/*`         | Image management routes  |
| *      | `/annotations/*`    | Annotation CRUD routes   |

---

## License

MIT
