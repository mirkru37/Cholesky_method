import Validation
import numpy as np

def upper(min_, message=""):
    n = input(message)
    if Validation.is_int(n):
        if int(n) >= int(min_):
            return int(n)
    return upper(min_, message)


def between(min_, max_, message=""):
    if max_ < min_:
        max_, min_ = min_, max_
    n = input(message)
    if Validation.is_number(n):
        if min_ <= n <= max_:
            return int(n) if Validation.is_int(n) else float(n)
    print("Invalid value")
    return between(min_, max_, message)


def int_(message=""):
    s = input(message)
    if Validation.is_int(s):
        return int(s)
    print("Invalid number!!!")
    return int_(message)


def number(message=""):
    n = input(message)
    if Validation.is_number(n):
        return int(n) if Validation.is_int(n) else float(n)
    print("Invalid number!!!")
    return number(message)


def matrix(message=""):
    matrix_ = []
    b = []
    n = upper(1, "Enter x count: ")
    for i in range(n):
        matrix_.append([])
        for j in range(n):
            matrix_[i].append(number(f"Input [{i}][{j}] element: "))
        b.append(number(f"Input result of row {i}:"))
    return np.array(matrix_), b
