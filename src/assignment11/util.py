import numpy as np
def min_max(rows, cols, elements):
    array = np.array(elements, dtype=int).reshape(rows, cols)
    min_values = np.min(array, axis=1)
    max_min_values = np.max(min_values)
    return max_min_values




