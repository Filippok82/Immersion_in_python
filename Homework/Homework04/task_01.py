"""Напишите функцию для транспонирования матрицы"""

import numpy as np


def matrix_transposition01(mat: list) -> list:
    result01 = np.transpose(matrix)
    return result01



def matrix_transposition02(mat: list) -> list:
    result02 = [list(i) for i in zip(*matrix)]
    return result02


matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_transposition01(matrix))
print()
print(matrix_transposition02(matrix))



