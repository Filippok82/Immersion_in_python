"""Напишите программу, которая использует модуль logging для
вывода сообщения об ошибке в файл.
Например отлавливаем ошибку деления на ноль."""

import logging

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.ERROR, filename='ZeroDivisionError.log', encoding='utf-8',
                    format=FORMAT, style="{")
logger = logging.getLogger(__name__)


def func_div_two(a, b) -> float:
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(f'Ошибка деления числа {a} на число {b}')
        return float('inf')
    return res


if __name__ == '__main__':
    print(func_div_two(8, 0))