# Функции “из коробки”

# Функция map()

# texts = ["Привет", "ЗДОРОВА", "привеТствую"]
# res = map(lambda x: x.lower(), texts)
# print(*res)


# Функция filter()

# numbers = [42, -73, 1024]
# res = tuple(filter(lambda x: x > 0, numbers))
# print(res)

#Функция zip()

# names = ["Иван", "Николай", "Пётр"]
# salaries = [125_000, 96_000, 109_000]
# awards = [0.1, 0.25, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary * award:.2f}')

# Функция max()

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",109_000)]
# print(max(lst_1, default='empty'))
# print(max(*lst_2))
# print(max(lst_3, key=lambda x: x[1]))

# Функция min()

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр",
# 109_000)]
# print(min(lst_1, default='empty'))
# print(min(*lst_2))
# print(min(lst_3, key=lambda x: x[1]))

# Функция sum()

# my_list = [42, 256, 73]
# print(sum(my_list))
# print(sum(my_list, start=1024))

#Функция all()


# def all_(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True


#_________________________________________________

# numbers = [42, -73, 1024]
# if all(map(lambda x: x > 0, numbers)):
#     print('Все элементы положительные')
# else:
#     print('В последовательности есть отрицательные и/или нулевые элементы')


# Функция any()

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

#____________________________________________________

# numbers = [42, -73, 1024]
# if any(map(lambda x: x > 0, numbers)):
#     print('Хотя бы один элемент положительный')
# else:
#     print('Все элементы не больше нуля')


# # Функция chr()
#
# print(chr(97))
# print(chr(1105))
# print(chr(128519))
#
# # Функция ord()
#
# print(ord('a'))
# print(ord('а'))
# print(ord('😉'))


# Функция locals()

# SIZE = 10
# def func(a, b, c):
#     x = a + b
#     print(locals())
#     z = x + c
#     return z
#
# func(1, 2, 3)

#Функция globals()

# SIZE = 10
# def func(a, b, c):
#     x = a + b
#     print(globals())
#     z = x + c
#     return z
#
# print(globals())
# print(func(1, 2, 3))
#
# x = 42
# glob_dict = globals()
# glob_dict['x'] = 73
# print(x)


print(vars(int))

data = [25, -42, 146, 73, -100, 12]
print(list(map(str, data)))
print(max(data, key=lambda x: -x))
print(*filter(lambda x: not x[0].startswith('__'),
globals().items()))