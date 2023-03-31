"""Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов."""

__all__ = ['my_function02']

from random import randint as rnd


def deco(func):
    def wrapper(number: int, count: int):
        if number < 1 or number > 100:
            number = rnd(1, 100)
        if count < 1 or count > 10:
            count = rnd(1, 10)
        result = func(number, count)
        return result

    return wrapper


@deco
def my_function02(number: int, count: int) -> None:
    print(f' у вас {count} попыток')
    for i in range(count):
        num = int(input(f"Введите число от 1 до 100 "))
        if num > number:
            print("Число введенное больше")
        elif num < number:
            print("Число введенное меньше")
        else:
            print('Вы угадали')
            break


my_function02(333, 15)
