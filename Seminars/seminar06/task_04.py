"""Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны."""

from random import randint as rnd


def my_function04(text: str, a: list, c: int) -> int:
    print(riddle)
    for i in range(c):
        anv = input("Введите ответ ")
        if anv in answers:
            return i + 1
    return 0


if __name__ == '__main__':
    riddle = 'Какой орган спасает тушканчика от перегрева?'
    answers = ['уши', 'нос', 'хвост', 'лапы']
    count = int(5)
    print(my_function04(riddle, answers, count))

