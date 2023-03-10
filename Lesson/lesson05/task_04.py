# Создание функции генератора

# def factorial(n):
#     number = 1
#     result = []
#     for i in range(1, n + 1):
#         number *= i
#         result.append(number)
#     return result
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')


# Команда yield

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
# for i, num in enumerate(factorial(10), start=1):
#     print(f'{i}! = {num}')

# Функции iter и next для генераторов

# def factorial(n):
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#         yield number
#
# my_iter = iter(factorial(4))
# print(my_iter)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter)) # StopIteration


def gen(a: int, b: int) -> str:
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        yield str(i)

for item in gen(10, 1):
    print(f'{item = }')
