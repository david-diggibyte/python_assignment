import numpy as np
def calculating_determinant(n, matrix_elements):
    matrix = np.array(matrix_elements, dtype=float).reshape(n, n)
    determinant_value = round(np.linalg.det(matrix), 2)
    return determinant_value

