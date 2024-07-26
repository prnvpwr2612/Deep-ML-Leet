def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = []
    for i in a:
        arr = [j for j in zip(*a)]
        b.append(arr)
        break
    return b