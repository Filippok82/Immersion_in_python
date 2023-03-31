"""�апишите следующие функции:

Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса code"""
import csv
import json
import random
from typing import Callable


def read_csv(func: Callable):
    def wrapper(*args, **kwargs):
        with open('hw09.csv', 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                args = (int(j) for j in row)
                result = func(*args, **kwargs)
                yield result

    return wrapper


def convert_json(func: Callable):
    def wrapper(*args, **kwargs):
        json_file = []
        for result in func(*args, **kwargs):
            dct = {'args': args, **kwargs, 'result': str(result)}
            json_file.append(dct)
        with open('hw09.json', 'w') as json_f:
            json.dump(json_file, json_f, indent=2)

    return wrapper


@convert_json
@read_csv
def root_equation(a: int, b: int, c: int):
    if a != 0:
        disc = b * b - 4 * a * c
        x1 = (-b + disc ** 0.5) / (2 * a)
        x2 = (-b - disc ** 0.5) / (2 * a)
        return disc, x1, x2
    else:
        return 0, 0, 0


def write_csv(row_c: int):
    rows = []
    for _ in range(row_c):
        a, b, c = [random.randint(-20, 20) for _ in range(3)]
        rows.append({'a': a, 'b': b, 'c': c})
    with open('hw09.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ['a', 'b', 'c']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    row_count = 500
    root_equation()
    write_csv(row_count)
