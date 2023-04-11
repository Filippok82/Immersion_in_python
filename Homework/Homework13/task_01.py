""" Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода..
"""

"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""

from exception_13 import UserValueError
from math import pi


class Circle:
    def __init__(self, radius: float):
        if radius <= 0:
            raise UserValueError
        else:
            self.radius = radius

    def length_circle(self):
        return 2 * pi * self.radius

    def area_circle(self):
        return pi * self.radius ** 2


if __name__ == '__main__':
    # my_circle = Circle(39)
    my_circle1 = Circle(0)
    # print(my_circle.length_circle(), my_circle.area_circle())
    print(my_circle1.length_circle(), my_circle1.area_circle())
