"""Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""

from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def length_circle(self):
        return 2 * pi * self.radius

    def area_circle(self):
        return pi * self.radius ** 2

my_circle = Circle(10)
print(my_circle.length_circle(),my_circle.area_circle())