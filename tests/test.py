import requests

data = {
    "matrix_m": [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5]
    ],
    "vector_x": [1, 1, 1, 1, 1],
    "vector_b": [0, 0, 0, 0, 0]
}

response = requests.post("http://localhost:8000/calculate", json=data)
print(response.json())