"""Области видимости"""


# def func(a):
#     x = 1
#     res = x + a
#     return res
#
#
# x = 100
# print(func(5))


# Функция как объект высшего порядка

# def add_str(a: str, b: str) -> str:
#     return a + ' ' + b
#
#
# print(add_str('Hello', 'world!'))

# ПЕРЕПИШЕМ верхнюю фнукцию

# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
#
# print(add_one_str('Hello')('world!'))


# Замыкаем функцию с параметрами

# from typing import Callable
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     def add_two_str(b: str) -> str:
#         return a + ' ' + b
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('world!'))
# print(hello('friend!'))
# print(bye('wonderful world!'))
#
# print(f'{type(add_one_str) = }, {add_one_str.__name__ = },{id(add_one_str) = }')
# print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
# print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')

# Замыкаем изменяемые и неизменяемые
# объекты

# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     names = []
#     def add_two_str(b: str) -> str:
#         names.append(b)
#         return a + ', ' + ', '.join(names)
#     return add_two_str
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))


# заменим list на  неизменяемый str

# from typing import Callable
#
#
# def add_one_str(a: str) -> Callable[[str], str]:
#     text = ''
#
#     def add_two_str(b: str) -> str:
#         nonlocal text
#         text += ', ' + b
#         return a + text
#     return add_two_str
#
#
# hello = add_one_str('Hello')
# bye = add_one_str('Good bye')
#
# print(hello('Alex'))
# print(hello('Karina'))
# print(bye('Alina'))
# print(hello('John'))
# print(bye('Neo'))

# 