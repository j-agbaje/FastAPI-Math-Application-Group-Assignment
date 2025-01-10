from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from typing import List
import math

app = FastAPI()

class MatrixInput(BaseModel):
    matrix_m: List[List[float]]  # 5x5 matrix M
    vector_x: List[float]        # 5x1 vector X
    vector_b: List[float]        # 5x1 vector B

def sigmoid(x: float) -> float:
    """Apply sigmoid activation function."""
    return 1 / (1 + math.exp(-x))

def matrix_multiply_manual(matrix_m: List[List[float]], vector_x: List[float]) -> List[float]:
    """Perform matrix multiplication without NumPy."""
    rows = len(matrix_m)
    result = []
    
    for i in range(rows):
        element_sum = 0
        for j in range(len(vector_x)):
            element_sum += matrix_m[i][j] * vector_x[j]
        result.append(element_sum)
    
    return result

def validate_input_dimensions(data: MatrixInput):
    """Validate input dimensions."""
    if len(data.matrix_m) != 5 or any(len(row) != 5 for row in data.matrix_m):
        raise HTTPException(status_code=400, detail="Matrix M must be 5x5")
    if len(data.vector_x) != 5:
        raise HTTPException(status_code=400, detail="Vector X must have length 5")
    if len(data.vector_b) != 5:
        raise HTTPException(status_code=400, detail="Vector B must have length 5")

@app.post("/calculate")
async def calculate(data: MatrixInput):
    """Calculate (M * X) + B with and without NumPy, then apply sigmoid."""
    validate_input_dimensions(data)
    
    # Manual calculation
    manual_mx = matrix_multiply_manual(data.matrix_m, data.vector_x)
    manual_result = [x + b for x, b in zip(manual_mx, data.vector_b)]
    manual_sigmoid = [sigmoid(x) for x in manual_result]
    
    # NumPy calculation
    numpy_m = np.array(data.matrix_m)
    numpy_x = np.array(data.vector_x)
    numpy_b = np.array(data.vector_b)
    
    numpy_result = np.dot(numpy_m, numpy_x) + numpy_b
    numpy_sigmoid = 1 / (1 + np.exp(-numpy_result))
    
    return {
        "manual_calculation": {
            "mx_plus_b": manual_result,
            "sigmoid": manual_sigmoid
        },
        "numpy_calculation": {
            "mx_plus_b": numpy_result.tolist(),
            "sigmoid": numpy_sigmoid.tolist()
        }
    }

@app.get("/")
async def root():
    """Root endpoint with usage instructions."""
    return {
        "message": "Matrix Calculator API",
        "usage": {
            "endpoint": "/calculate",
            "method": "POST",
            "input_format": {
                "matrix_m": "5x5 matrix",
                "vector_x": "5x1 vector",
                "vector_b": "5x1 vector"
            }
        }
    }
