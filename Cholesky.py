import numpy as np


def find_y(L, b):
    res = []
    for i, b_i in enumerate(b):
        sum_ = 0
        for k in range(i):
            sum_ += L[i][k] * res[k]
        res.append((b_i - sum_) / L[i][i])
    return res


def find_x(L_T, y):
    res = np.zeros(len(L_T[0]))
    for i, y_i in reversed(list(enumerate(y))):
        sum_ = 0
        for k in range(i + 1, len(L_T[0])):
            sum_ += L_T[i][k] * res[k]
        res[i] = ((y_i - sum_) / L_T[i][i])
    return res


def cholesky(A, b):
    L = np.linalg.cholesky(A)
    if (A != np.dot(L, L.T)).all():
        raise ValueError("Asymmetrical matrix")
    print(L)
    y = find_y(L, b)
    x = find_x(L.T, y)
    return x
