import numpy as np

def to_categorical(x, n_col=None):
    if not n_col:
        n_col = np.amax(x) + 1
    print(x.shape[0])
    one_hot = np.zeros((x.shape[0], n_col))
    print(np.arange(x.shape[0]))
    print(x)
    one_hot[np.arange(x.shape[0]), x] = 1
    return one_hot

A = np.array([8,5,6])
print(to_categorical(A))