"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""


def my_fanction01(p: str):
    print(p)
    p1 = []
    p2 = []
    p3 = []
    p1.append(p.split('/')[:-1])
    p2.append(p.split('/')[-1:])
    p3.append(p.split('.'))
    print(p1)
    print(p2)
    print(p3)
    res = tuple()


path = 'C:/Python/PythonGB/Lesson/lesson01/lesson_01.py'

my_fanction01(path)


# extension = '/path/to/somefile.ext'.split('.')[-1]
# print(extension)

