"""Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры
используйте генераторное выражение."""

from sys import argv
from random import randint as rnd


def my_function02(a: int = 0, b: int = 100, c: int = 5) -> bool:
    number = rnd(a, b)
    for i in range(c):
        print(f"Введите число от {num1} до {num2} ")
        num = int(input())
        if num > number:
            print("Число введенное больше")
        elif num < number:
            print("Число введенное меньше")
        else:
            return True
    return False


if __name__ == '__main__':
    num, *params = argv

    print(my_function02(*(int(n) for n in params)))
