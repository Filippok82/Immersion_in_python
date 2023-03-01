# Множества set и frozenset

# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'

# Методы множеств
# Метод add
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
# my_set.add((9, 10))
# print(my_set)

# Метод remove
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.remove(5)
# print(my_set)
# my_set.remove(10) # KeyError: 10

# Метод discard
# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.discard(5)
# print(my_set)
# my_set.discard(10)

# Метод intersection
# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# Метод union

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Метод difference

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

# Проверка на вхождение, in
# my_set = {3, 4, 2, 5, 6, 1, 7}
# print(2 in my_set)
# print(42 in my_set)

# Классы bytes и bytearray

text_en = 'Hello world!'
res = text_en.encode('utf-8')
print(res, type(res))
text_ru = 'Привет, мир!'
res = text_ru.encode('utf-8')
print(res, type(res))

x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
print(f'{x = }\n{y = }')

