"""Функция получает на вход список чисел.
✔ Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
✔ Как вариант напишите сортировку пузырьком.
Её описание есть в википедии"""


def my_func04(a: list) -> None:
    n = 1
    while n < len(a):
        for i in range(len(a) - n):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        n += 1


my_list = list((23, 12, 14, 25, 5, 22, 9999, 3))
my_func04(my_list)
print(my_list)
