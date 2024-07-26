import numpy as np

def to_categorical(x,n_col=None):
    array_result=np.array()
    arrayi = np.array()
    for i in range(x):
        if i == x[i]:
            arrayi[i]=1
        else:
            arrayi[i]=0
        array_result.append(arrayi)
    return array_result
A = np.array([2,3,4])
print(to_categorical(A))