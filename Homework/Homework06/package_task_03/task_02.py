"""Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь."""

from random import randint as rnd


def my_function02(a: int, b: int, c: int) -> bool:
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
    num1 = int(input("Введите первое число:"))
    num2 = int(input("Введите второе число:"))
    chanse = int(input("Сколько попыток:"))
    print(my_function02(num1, num1, chanse))
