"""✔ Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
"""
from random import randint
import os

__all__ = ['gen_file']
__all__ = ['expansion', 'count_file']
MAX_LONG = 30
MIN_LONG = 6
MIN_BAIT = 256
MAX_BAIT = 4096
CHAR = 'abcdefghijklmnopqrstuvwxyz'


def gen_file(ex: list, c: 42):
    for _ in range(count_file):
        name_file = ""
        for _ in range(randint(MIN_LONG, MAX_LONG)):
            name_file += CHAR[randint(0, len(CHAR) - 1)]
        name_file += '.'
        name_file += ex[randint(0, len(ex) - 1)]
        print(name_file)
        with open(name_file, 'wb', buffering=0) as f1:
            f1.write(b'X' * randint(MIN_BAIT, MAX_BAIT))
        print(os.path.getsize(f'C:\Python\PythonGB\Seminars\seminar07\{name_file}'))


expansion = ['txt', 'doc', 'md']
count_file = 1
gen_file(expansion, count_file)
