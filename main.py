import Input
import Cholesky
import numpy as np

if __name__ == "__main__":
    matrix, b = Input.matrix("Please input matrix: ")  # [[4, 2, 2, 1], [2, 5, 1, 2], [2, 1, 5, 1], [1, 2, 1, 4.875]], [9, 10, 9, 8.875]  # Input.matrix("Please input matrix: ")
    print("Your matrix: \n", matrix)
    print("Your b:", b)
    try:
        res = Cholesky.cholesky(matrix, b)
        print("Results: ", res)
    except Exception as e:
        print(e)
