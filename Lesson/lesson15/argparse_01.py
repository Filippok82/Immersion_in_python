"""5. Модуль argparse
"""

# import argparse
#
# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float,
#                     nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано: {args}')

"""Создаём парсер, ArgumentParser"""
# import argparse
#
# parser = argparse.ArgumentParser(prog='average', description='My first argument parser',
#                                  epilog='Returns the arithmetic mean')
#
# parser.add_argument('numbers', metavar='N', type=float,
#                     nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'В скрипт передано: {args}')

"""Выгружаем результаты, parse_args"""

# import argparse
#
# parser = argparse.ArgumentParser(description='My first argument parser')
# parser.add_argument('numbers', metavar='N', type=float,
#                     nargs='*', help='press some numbers')
# args = parser.parse_args()
# print(f'Получили экземпляр Namespace: {args = }')
# print(f'У Namespace работает точечная нотация: {args.numbers = }')
# print(f'Объекты внутри могут быть любыми: {args.numbers[1] = }')


"""Добавляем аргументы, add_argument"""

import argparse


def quadratic_equations(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    if d == 0:
        return -b / (2 * a)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Solving quadratic equations')
    parser.add_argument('param', metavar='a b c', type=float,
                        nargs=3, help='enter a b c separated by a space')
    args = parser.parse_args()
    print(quadratic_equations(*args.param))

"""Необязательные аргументы и значения по умолчанию
Изменим наш парсер и добавим ещё несколько параметров к аргументам."""

import argparse

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None
#
#
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(description='Solving quadratic equations')
#     parser.add_argument('-a', metavar='a', type=float,
#                         help='enter a for ax^2+bx+c=0', default=1)
#     parser.add_argument('-b', metavar='b', type=float,
#                         help='enter b for ax^2+bx+c=0', default=0)
#     parser.add_argument('-c', metavar='c', type=float,
#                         help='enter c for ax^2+bx+c=0', default=0)
#     args = parser.parse_args()
#     print(quadratic_equations(args.a, args.b, args.c))

"""Параметр action для аргумента
И напоследок ещё один интересный параметр уже без квадратных уравнений. Речь
пойдёт о параметре action."""
import argparse

parser = argparse.ArgumentParser(description='Sample')
parser.add_argument('-x', action='store_const', const=42)
parser.add_argument('-y', action='store_true')
parser.add_argument('-z', action='append')
parser.add_argument('-i', action='append_const', const=int,
                    dest='types')
parser.add_argument('-f', action='append_const', const=float,
                    dest='types')
parser.add_argument('-s', action='append_const', const=str,
                    dest='types')
args = parser.parse_args()
print(args)
