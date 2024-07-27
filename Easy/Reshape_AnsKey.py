import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int|float]) -> list[list[int|float]]:
    return np.array(a).reshape(new_shape).tolist()