import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode=='row':
        means = np.mean(matrix, axis=1)
    else:
        means = np.mean(matrix, axis=0)
    return means

K= [[1,2,3],[1,2,3],[1,2,3]]
print(calculate_matrix_mean(K,'row'))