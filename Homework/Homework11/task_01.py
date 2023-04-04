"""Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
"""
from random import randint


class Matrix:
    """Создание класса матрица для для сложения,
        сравнения, вывода на печать и умножения"""

    def __init__(self, m: int, n: int) -> list:
        """Создание мартицы"""
        self.m = m
        self.n = n
        matrix = [[randint(1, 10) for j in range(self.n)] for i in range(self.m)]

        self.matrix = matrix

    def __str__(self):
        """Вывод на печать"""
        return f'Matrix{self.matrix}\n'

    def __add__(self, other):

        num_str = len(self.matrix)
        num_col = len(other.matrix[0])
        for i in range(num_str):
            for j in range(num_col):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            result = self.matrix
        return f'Результат сложения {result}'

    def __eq__(self, other):
        num_str = len(self.matrix)
        num_col = len(other.matrix[0])
        for i in range(num_str):
            for j in range(num_col):
                self.matrix[i][j] = self.matrix[i][j] == other.matrix[i][j]
            result = self.matrix
        return f'Результат на идентичность {result}'

    def __lt__(self, other):
        num_str = len(self.matrix)
        num_col = len(other.matrix[0])
        for i in range(num_str):
            for j in range(num_col):
                self.matrix[i][j] = self.matrix[i][j] < other.matrix[i][j]
            result = self.matrix
        return f'Результат на меньше {result}'


mat1 = Matrix(3, 3)
mat2 = Matrix(3, 3)
print(mat1, mat2)
mat3 = mat1 + mat2
mat5 = mat1 < mat2
print(mat3)
print(mat1 == mat2)
print(mat5)
