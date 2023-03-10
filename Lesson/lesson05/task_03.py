# Генераторы

# a = range(0, 10, 2)
# print(f'{a=}, {type(a)=}, {a.__sizeof__()=}, {len(a)}')
# b = range(-1_000_000, 1_000_000, 2)
# print(f'{b=}, {type(b)=}, {b.__sizeof__()=}, {len(b)}')


# Генераторные выражения

# my_gen = (chr(i) for i in range(97, 123))
# print(my_gen) # <generator object <genexpr> at 0x000001ED58DD7D60>
# for char in my_gen:
#     print(char)

# ____________________________________________________

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1)
# res = list(mult)
# print(f'{len(res)=}\n{res}')


# List comprehensions

# my_listcomp = [chr(i) for i in range(97, 123)]
# print(my_listcomp) # ['a', 'b', 'c', 'd', ..., z]
# for char in my_listcomp:
#     print(char)

# _______________________________________________________

# Длинный код:

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = []
# for item in data:
#     if item % 2 == 0:
#         res.append(item)
# print(f'{res = }')

# Аналогичное решение, но с использованием синтаксического сахара listcomp:

# data = [2, 5, 1, 42, 65, 76, 24, 77]
# res = [item for item in data if item % 2 == 0]
# print(f'{res = }')

# Генераторные выражения или генерация  списка

# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# res = [i + j for i in x if i % 2 != 0 for j in y if j != 1] # генерация списка
# print(f'{len(res)=}\n{res}')
#
# mult = (i + j for i in x if i % 2 != 0 for j in y if j != 1) # генерация выражения
# for item in mult:
#     print(f'{item = }')


# Set comprehensions множество

# my_setcomp = {chr(i) for i in range(97, 123)}
# print(my_setcomp)  # {'f', 'g', 'b', 'j', 'e',... }
# for char in my_setcomp:
#     print(char)
#
# x = [1, 1, 2, 3, 5, 8, 13]
# y = [1, 2, 6, 24, 120, 720]
# print(f'{len(x)=}\t{len(y)=}')
# res = {i + j for i in x if i % 2 != 0 for j in y if j != 1}
# print(f'{len(res)=}\n{res}')


# Dict comprehensions словари

# my_dictcomp = {i: chr(i) for i in range(97, 123)}
# print(my_dictcomp) # {97: 'a', 98: 'b', 99: 'c',... }
# for number, char in my_dictcomp.items():
#     print(f'dict[{number}] = {char}')


