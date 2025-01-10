# Matrix Calculator API

A FastAPI application that performs matrix multiplication with and without NumPy and applies sigmoid activation function.

## Features
- Matrix multiplication implementation (with and without NumPy)
- Sigmoid activation function
- Input validation
- REST API endpoint

## Installation
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `.\venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running the Application
```bash
uvicorn app.main:app --reload
```

## API Usage
POST request to `/calculate` with JSON body:
```json
{
    "matrix_m": [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]],
    "vector_x": [1,1,1,1,1],
    "vector_b": [0,0,0,0,0]
}
```