# Simple API Project

A standard RESTful API built with [FastAPI](https://fastapi.tiangolo.com/), demonstrating core operations using an in-memory database.

## Features

*   **FastAPI Framework:** Fast, modern, and high-performance web framework.
*   **Data Validation:** Handled effortlessly using Pydantic models.
*   **Endpoints:**
    *   `POST /items` - Create a new item
    *   `GET /items` - Retrieve a list of all items
    *   `DELETE /items/{item_id}` - Delete a specific item by its `id`
*   **Interactive API Docs:** Automatic Swagger UI and ReDoc documentation.

## Prerequisites

*   Python 3.8 or higher

## Setup & Installation

Follow these steps to get the development environment running locally:

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd api-project
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   
   # On macOS and Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Make sure your virtual environment is still activated.
2. Start the local server using `uvicorn`:
   ```bash
   uvicorn app.main:app --reload
   ```
3. The API will now be running at: `http://127.0.0.1:8000`

## API Documentation

FastAPI automatically generates interactive API documentation. You can test your endpoints directly from the browser:

*   **Swagger UI (Interactive):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
*   **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```text
api-project/
├── app/
│   ├── main.py      # Entry point and FastAPI application instance
│   ├── models.py    # Pydantic data models for request/response validation
│   └── routes.py    # API endpoints and router configuration
├── requirements.txt # Locked project dependencies
└── README.md        # Project documentation
```