# Строгая динамическая типизация Python

# a = 5
# print(type(a), id(a))
# a = "hello world"
# print(type(a), id(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a), id(a))

#__________________________________________________________
# data = 42
# print(isinstance(data, int))
#
# data = True
# print(isinstance(data, int))
#
# data = 3.14
# print(isinstance(data, (int, float, complex)))

#_____________________________________________________
# num = 2 + 2 * 2
# digit = 36 / 6
# print(num, digit)
# print(num == digit)
# print(num is digit)

# Изменяемые и неизменяемые типы

# txt = 'Hello world!'
# txt[5] = '_'

#_________________________________________________________
# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))

#__________________________________________________________

# a = с = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))

# Хэш hash() как проверка на неизменяемость

# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(hash(my_list)) # получим ошибку, т.к. list изменяемый

#  Задание №1
# Напишите небольшую программу, которая запрашивает у пользователя любой текст
# и выводит о нём следующую информацию:
# ● тип объекта,
# ● адрес объекта в оперативной памяти,
# ● хеш объекта.
# Результат работы пришлите в чат. У вас 5 минут


a = input('Введите текст: ')
print(type(a), id(a), hash(a))