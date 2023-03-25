# 2. Простой декоратор без параметров
# Передача функции в качестве аргумента

# import time
# from typing import Callable
#
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#
#         return result
#
#     return wrapper
#
#
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')
# control = main(factorial)
# print(f'{control.__name__ = }')
# print(f'{control(1000) = }')


# Синтаксический сахар Python, @

# import time
# from typing import Callable
#
#
# def main(func: Callable):
#     def wrapper(*args, **kwargs):
#         print(f'Запуск функции {func.__name__} в {time.time()}')
#         result = func(*args, **kwargs)
#         print(f'Результат функции {func.__name__}: {result}')
#         print(f'Завершение функции {func.__name__} в {time.time()}')
#         return result
#
#     return wrapper
#
#
# @main
# def factorial(n: int) -> int:
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# print(f'{factorial(1000) = }')

# Множественное декорирование

# from typing import Callable
#
#
# def deco_a(func: Callable):
#     def wrapper_a(*args, **kwargs):
#         print('Старт декоратора A')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора A')
#         return res
#     print('Возвращаем декоратор A')
#     return wrapper_a
#
#
# def deco_b(func: Callable):
#     def wrapper_b(*args, **kwargs):
#         print('Старт декоратора B')
#
#
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора B')
#         return res
#     print('Возвращаем декоратор B')
#     return wrapper_b
#
#
# def deco_c(func: Callable):
#     def wrapper_c(*args, **kwargs):
#         print('Старт декоратора C')
#         print(f'Запускаю {func.__name__}')
#         res = func(*args, **kwargs)
#         print(f'Завершение декоратора C')
#         return res
#     print('Возвращаем декоратор C')
#     return wrapper_c
#
#
# @deco_c
# @deco_b
# @deco_a
# def main():
#     print('Старт основной функции')
#
# if __name__ == '__main__':
#     print(":::: Запуск основной функции")
#     main()
#     print(":::: Завершение main")

# Дополнительные переменные в декораторе

from typing import Callable


def cache(func: Callable):
    _cache_dict = {}

    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
            return _cache_dict[args]

    return wrapper

@cache
def factorial(n: int) -> int:
    print(f'Вычисляю факториал для числа {n}')
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(10) = }')
print(f'{factorial(15) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
print(f'{factorial(10) = }')
print(f'{factorial(20) = }')
