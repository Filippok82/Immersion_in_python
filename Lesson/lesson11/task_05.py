"""5. Сравнение экземпляров класса"""
"""Сравнение на идентичность, __eq__"""


# class Triangle:
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b},{self.c}'
#
#     def __eq__(self, other):
#         return self is other
#
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# print(one == two)
# print(one == three)

# _________________________________________________

#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __str__(self):
#         return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
#
#     def __eq__(self, other):
#         first = sorted((self.a, self.b, self.c))
#         second = sorted((other.a, other.b, other.c))
#         return first == second
#
#
# one = Triangle(3, 4, 5)
# two = one
# three = Triangle(3, 4, 5)
# four = Triangle(4, 3, 5)
# print(f'{one == two = }')
# print(f'{one == three = }')
# print(f'{one == four = }')
# print(f'{one != one = }')


"""Сравнение на больше и меньше"""


from math import sqrt


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        return f'Треугольник со сторонами: {self.a}, {self.b}, {self.c}'
    def __repr__(self):
        return f'Triangle({self.a}, {self.b}, {self.c})'
    def __eq__(self, other):
        first = sorted((self.a, self.b, self.c))
        second = sorted((other.a, other.b, other.c))
        return first == second
    def area(self):
        p = (self.a + self.b + self.c) / 2
        _area = sqrt(p * (p - self.a) * (p - self.b) * (p -
        self.c))
        return _area
    def __lt__(self, other):
        return self.area() < other.area()
one = Triangle(3, 4, 5)
two = Triangle(5, 5, 5)
print(f'{one} имеет площадь {one.area():.3f} у.е.²')
print(f'{two} имеет площадь {two.area():.3f} у.е.²')
print(f'{one > two = }\n{one < two = }')
data = [Triangle(3, 4, 5), Triangle(6, 2, 5), Triangle(4, 4, 4), Triangle(3, 5, 3)]
result = sorted(data)
print(result)
print(', '.join(f'{item.area():.3f}' for item in result))