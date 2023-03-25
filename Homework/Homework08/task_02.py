"""Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов."""

from PythonGB.Seminars.seminar08.task_01 import convert
from PythonGB.Seminars.seminar08.task_02 import name_id_access_level
from task_01 import directory_traversal

hw = directory_traversal('C:\Python\PythonGB\Homework\Homework08')
convert(file_name='new_file.txt')
name_id_access_level('ident.json')
