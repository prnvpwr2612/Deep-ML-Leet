import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    a_new = np.array(a)
    new_row = new_shape[0]
    new_column = new_shape[1]
    reshaped_matrix = a_new.reshape(new_row,new_column)
    c = reshaped_matrix.tolist()
    return c