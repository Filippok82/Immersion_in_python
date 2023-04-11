"""Создать unittest к задаче:
 Класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""
import unittest
from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def length_circle(self):
        result1 = 2 * pi * self.radius
        return f"{result1:.3f}"

    def area_circle(self):
        result2 = pi * self.radius ** 2
        return f"{result2:.3f}"


class TestCaseName(unittest.TestCase):

    def setUp(self) -> None:
        self.c1 = Circle(10)
        self.c2 = Circle(22)

    def test_length(self):
        self.assertEqual(self.c1.length_circle(), '62.832')

    def test_area(self):
        self.assertEqual(self.c2.area_circle(), '1520.531')


if __name__ == '__main__':
    unittest.main(verbosity=2)
