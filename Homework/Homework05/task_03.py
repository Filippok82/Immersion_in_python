"""Создайте функцию генератор чисел Фибоначчи (см. Википедию)."""

n = int(input('Введите число: '))


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


f = fib()
for _ in range(n):
    print(next(f))
