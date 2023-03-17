"""Напишите функцию, которая заполняет файл
(добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. """

import random as rnd

MIN_LIMIT = -1000
MAX_LIMIT = 1000

def func01(cnt_line:int, file_name:str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(cnt_line):
            tmp_str = str(rnd.randint(MIN_LIMIT, MAX_LIMIT)) \
                    + "|" + str(rnd.uniform(MIN_LIMIT, MAX_LIMIT))
            print(tmp_str)
            f.write(f'{tmp_str}\n')

func01(5, "text_file.txt")

# import random as rnd
#
#
# def file_in(a: int, b: str) -> None:
#     with open('text_file.txt', 'w', encoding='utf-8') as f:
#         for i in range(a):
#             inumber = rnd.randint(-1000, 1000)
#             fnumber = rnd.uniform(-1000, 1000)
#
#             f.write(f'{str(inumber)} | {str(fnumber)} \n')
#
#
# file_in(5, 'text_file.txt')