# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

list01 = [1, 8, 5, 7, 12, 25, 4, 8, 12]
list02 = []

for i, item in enumerate(list01, start=1):
    if item % 2 != 0:
        list02.append(i)
print(list02)
