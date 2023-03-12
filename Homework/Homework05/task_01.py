"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""


<<<<<<< HEAD
def my_function(p: str) -> tuple:
    a = p.split('.')[0]
    b = p.split('/')[-1].split('.')[0]
    c = p.split('.')[1]
    print(a)  # оставила для проверки
    print(b)  # оставила для проверки
    print(c)  # оставила для проверки
    res = tuple(a + b + c)
    print(*res)


path = 'C:/Python/PythonGB/Lesson/lesson05/task_04.py'
my_function(path)
=======
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

>>>>>>> 9f01098586ec237d7e4887819668e2fe016ea52a
