import numpy as np

def to_categorical(x, n_col=None):
    array_result= []
    classes=max(x)+1
    arrayi = []
    for i in x:
        arrayi=[0]*classes
        arrayi[i]=1
        array_result.append(arrayi)
    return array_result

A = [2,3,4]
print(to_categorical(A))