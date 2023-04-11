"""Создать doctest к задаче:
 Класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь"""

from math import pi


def length_circle(radius: int):
    """
            >>> length_circle(10)
            '62.832'
            >>> length_circle(22)
            '138.230'
            """
    result1 = 2 * pi * radius
    return f"{result1:.3f}"


def area_circle(radius):
    """
            >>> area_circle(10)
            '314.159'
            >>> area_circle(22)
            '1520.531'
            """

    result2 = pi * radius ** 2
    return f"{result2:.3f}"


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
