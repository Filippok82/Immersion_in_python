"""Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""



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



