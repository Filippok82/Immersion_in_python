"""Напишите функцию, которая получает на вход директрорию и рекурсивно
обходит её и все вложенные директори. Результаты обхода сохранить в файлы json, csv, pickle
- для дочерних объектов указывать родительскую директорию
- для каждого объекта укажите файл это или директория
- для файлов сохраните его размер в байтах, а для директории размер файлов в ней
с учетом всех вложенных файлов"""

import csv
import json
import pickle
import os
from os.path import getsize, join

__all__ = ['directory_traversal']


def directory_traversal(direct: str):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []

    for dir_path, dir_name, file_name in os.walk(direct):
        json_data.setdefault(dir_path, {})  # получает/вставляет значение ключа
        for dir in dir_name:
            size = sum(getsize(join(dir_path, name)) for name in file_name)
            json_data[dir_path].update({dir: {'size': size, 'file_or_dir': 'directory'}})
            rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
        for fi in file_name:
            size = os.path.getsize(dir_path + '/' + fi)
            json_data[dir_path].update({fi: {'size': size, 'file_or_dir': 'file'}})
            rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})
        print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

    with open('hw08.json', 'w', encoding='utf-8') as f_json, \
            open('hw08.csv', 'w', newline='', encoding='utf-8') as f_csv, \
            open('hw08.pickle', 'wb') as f_pickle:
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(json_data, f_pickle, protocol=pickle.DEFAULT_PROTOCOL)


if __name__ == '__main__':
    path_dir = 'C:\Python\PythonGB\Homework\Homework08'
    directory_traversal(path_dir)
