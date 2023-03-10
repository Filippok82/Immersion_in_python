""" Итераторы """

# Функция iter

# a = 42
# iter(a)  # TypeError: 'int' object is not iterable

# ___________________________________________

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(list_iter)

# ________________________________________________

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(*list_iter)
# print(*list_iter)

# Второй параметр функции iter — sentinel

# data = [2, 4, 6, 8]
# list_iter = iter(data, 6) # TypeError: iter(v, w): v must be callable
# _____________________________________________________________-

# import functools
#
# f = open('mydata.bin', 'rb')
# for block in iter(functools.partial(f.read, 16), b''):
#     print(block)
# f.close()

# Функция next

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))  # StopIteration

#______________________________________________________________________

# data = [2, 4, 6, 8]
# list_iter = iter(data)
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))
# print(next(list_iter, 42))




