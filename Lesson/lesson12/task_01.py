"""1. Класс как функция"""

# class Number:
#     def __init__(self, num):
#         self.num = num
#
#
# n = Number(42)
# print(f'{callable(Number) = }')
# print(f'{callable(n) = }')


"""Метод вызова функции __call__"""

from collections import defaultdict


class Storage:
    def __init__(self):
        self.storage = defaultdict(list)

    def __str__(self):
        txt = '\n'.join((f'{k}: {v}' for k, v in
                         self.storage.items()))
        return f'Объекты хранилища по типам:\n{txt}'

    def __call__(self, value):
        self.storage[type(value)].append(value)
        return f'К типу {type(value)} добавлен {value}'


s = Storage()
print(s(42))
print(s(72))
print(s('Hello world!'))
print(s(0))
print(s)
