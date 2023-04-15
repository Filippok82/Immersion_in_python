"""
Задача: Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное
число за указанное число попыток.
Добавить  к ней логирование ошибок и полезной
информации. Также реализовать  возможность запуска из
командной строки с передачей параметров."""
import logging
from typing import Callable
import argparse
FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='task01.log',
                    encoding='utf-8', format=FORMAT, style="{")
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='My  arguments parser')
parser.add_argument('numbers', metavar='N', type=int, nargs='*', help='введите число')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

def deco(number: int, count: int) -> Callable[[], None]:
    def my_function01() -> None:
        print(f' у вас {count} попыток')
        for i in range(count):
            data = []
            try:
                num = int(input(f"Введите число от 1 до 100: "))
                data.append(num)
                try:
                    if num > number:
                        print("Число введенное больше")
                    elif num < number:
                        print("Число введенное меньше")
                    else:
                        print('Вы угадали')
                        break

                except ValueError as e:
                    logger.error(f'Ошибка ввода {e}')
                    return None
            except ValueError as e:
                logger.error(f'Ошибка ввода {e}')
                return None

            logger.info(f'Все варианты ввода попытка {i+1} - {data}')
    return my_function01


if __name__ == '__main__':
    game = deco(20, 5)
    game()

"""Скрипт для запуска в консоле"""
# python task_01.py 20 5