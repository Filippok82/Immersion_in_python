# Простые объекты
# Целые числа
# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')

#____________________________________________

# import sys
#
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP

#_______________________________________________________

# num = 7_901_123_456_789
# print(num)

#____________________________________________________________

# Функции bin(), oct(), hex()

# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)

# Вещественные числа, функция float()

# print(0.1 + 0.2)
# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi)

# Логические типы, функция bool()

# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения по умолчанию: '))
# level = num or DEFAULT
# print(level)

#_________________________________________________________

# name = input('Как вас зовут? ')
# if name:
#     print('Привет, ' + name)
# else:
#     print('Анонимус, приветствую')

#_____________________________________________________________________

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# while data:
#     print(data.pop())

#Строки, функция str()
#
# txt = 'Книга называется "Война и мир".'
# print(txt)

#_____________________________________________________
# class str(object):
#     """
#     str(object='') -> str
#     str(bytes_or_buffer[, encoding[, errors]]) -> str
# ...
#     """
#______________________________________________________________-

# text = 'Привет.' 'Как ты, друг?' 'Рад тебя видеть.'
# print(text)
#
# very_long_text = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A ab alias animi assumenda at aut ' \
#                 'commodi, consequatur cumque ea harum, hic id illum ipsam itaque laboriosam magnam minus nam nulla ' \
#                 'numquam obcaecati officia officiis porro possimus praesentium quaerat temporibus ullam veniam? '
#
# print(very_long_text)

#Конкатенация строк

# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
# " до ста лет, но длинна строки не должна превышать " + str(LIMIT) + ' символов.'
# print(text)

# Размер строки в памяти

# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())

#_________________________________________________________

#Задание №3
text = str(input('Введите текст: '))
n = int(text)
if text.isdigit():
    print(bin(n), oct(n), hex(n))
else:
   print(text.isascii())
