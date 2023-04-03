"""Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
 которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
 Задачи должны решаться через вызов методов экземпляра."""

from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius


class LengthCircle(Circle):

    def __init__(self, radius: float):
        super().__init__(radius)

    def length_circle(self):
        return 2 * pi * self.radius


class AreaCircle(Circle):
    def __init__(self, radius: float):
        super().__init__(radius)

    def area_circle(self):
        return pi * self.radius ** 2


my_circle = LengthCircle(10)
print(my_circle.length_circle())
area = AreaCircle(10)
print(area.area_circle())