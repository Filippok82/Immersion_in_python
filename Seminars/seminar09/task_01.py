"""Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное
число за указанное число попыток."""

from random import randint as rnd
from typing import Callable


def deco(number: int, count: int) -> Callable [[], None]:

    def my_function01() -> None:
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
    return my_function01


game = deco(20, 5)
game()