"""✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 2
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
Добавлена к ней логирование полезной информации
"""
import logging
import os
from random import randint

MAX_LONG = 30
MIN_LONG = 6
MIN_BAIT = 256
MAX_BAIT = 4096
CHAR = 'abcdefghijklmnopqrstuvwxyz'

FORMAT = '{asctime} {levelname} {funcName}->{lineno}: {msg}'
logging.basicConfig(level=logging.INFO, filename='task02.log',
                    encoding='utf-8', format=FORMAT, style="{")
logger = logging.getLogger(__name__)


def gen_file(ex: list, count: int):
    for _ in range(count):
        name_file = ""
        for _ in range(randint(MIN_LONG, MAX_LONG)):
            name_file += CHAR[randint(0, len(CHAR) - 1)]
        name_file += '.'
        name_file += ex[randint(0, len(ex) - 1)]
        print(name_file)
        with open(name_file, 'wb', buffering=0) as f1:
            f1.write(b'X' * randint(MIN_BAIT, MAX_BAIT))
        size = os.path.getsize(f'C:\Python\PythonGB\Homework\Homework15\{name_file}')
        print(size)
        logger.info(f'Создан файл - {name_file} с количеством байт {size}')


if __name__ == '__main__':
    expansion = ['txt', 'doc', 'md']
    count_file = 1
    gen_file(expansion, count_file)
