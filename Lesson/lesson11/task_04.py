""""4. Математика и логика в классах

Обычные методы

Сложение через __add__
"""

# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#
# a = Vector(2, 4)
# b = Vector(3, 7)
# c = a + b
# print(f'{a = }\t{b = }\t{c = }')

"""Сдвиг вправо, __rshift__"""
#
# from random import choices
#
#
# class Closet:
#     CLOTHES = ('брюки', 'рубашка', 'костюм', 'футболка', 'перчатки', 'носки', 'туфли')
#
#     def __init__(self, count: int, storeroom=None):
#         self.count = count
#         if storeroom is None:
#             self.storeroom = choices(self.CLOTHES, k=count)
#         else:
#             self.storeroom = storeroom
#
#     def __str__(self):
#         names = ', '.join(self.storeroom)
#         return f'Осталось вещей в шкафу {self.count}:\n{names}'
#
#     def __rshift__(self, other):
#         shift = self.count if other > self.count else other
#         self.count -= shift
#         return Closet(self.count, choices(self.storeroom, k=self.count))
#
#
# storeroom = Closet(10)
# print(storeroom)
# for _ in range(4):
#     storeroom = storeroom >> 3
# print(storeroom)

"""Right методы
Умножение текста на “продвинутый текст”
методом __rmul__
"""

#
# class StrPro(str):
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args, **kwargs)
#         return instance
#
#     def __rmul__(self, other: str):
#         words = other.split()
#         result = self.join(words)
#         return StrPro(result)
#
#
# text = 'Каждый охотник желает знать где сидит фазан'
# s = StrPro(' (=^.^=) ')
# print(f'{text = }\n{s = }')
# print(text * s)
# print(s * text)  # TypeError: 'str' object cannot be interpreted as an integer


"""In place методы

Вычисление процентов вместо нахождения
остатка от деления, __imod__"""


from decimal import Decimal


class Money:
    def __init__(self, value: int | float):
        self.value = Decimal(value)
    def __repr__(self):
        return f'Money({self.value:.2f})'
    def __imod__(self, other):
        self.value = self.value * Decimal(1 + other / 100)
        return self


m = Money(100)
print(m)
m %= 50
print(m)
m %= 100
print(m)