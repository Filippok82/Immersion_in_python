"""Создать pytest к задаче:
 Класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""

from math import pi
import pytest


def length_circle(radius: int):
    result1 = 2 * pi * radius
    return f"{result1:.3f}"


def test_length_circle():
    assert length_circle(10) == '62.832', 'первая проверка метода length_circle'


def test_length_circle02():
    assert length_circle(22) == '138.230', 'вторая  проверка метода length_circle'


def area_circle(radius: int):
    result2 = pi * radius ** 2
    return f"{result2:.3f}"


def test_area_circle():
    assert area_circle(10) == '314.159', 'первая проверка методв area_circle'


def test_area_circle02():
    assert area_circle(22) == '1520.531', 'первая проверка методв area_circle'


if __name__ == '__main__':
    pytest.main(['-vv'])
