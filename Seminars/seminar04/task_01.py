# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


# def my_func01(a: str):
#     my_str02 = a.split()
#     my_str02.sort()
#     temp = 0
#     for item in my_str02:
#         if len(item) > temp:
#             temp = len(item)
#     for i, item in enumerate(my_str02, start=1):
#         print(f'{i} {item:>{temp}}')
#
# my_str01 = input('Введите строку:')
# my_func01(my_str01)


#________________________________________

def my_func01(a: str) -> None:

    my_str02 = sorted(a.split())
    max_len = len(max(my_str02,key=len))

    for i, item in enumerate(my_str02, start=1):
        print(f'{i} {item:>{max_len}}')

my_str01 = input('Введите строку:')
my_func01(my_str01)