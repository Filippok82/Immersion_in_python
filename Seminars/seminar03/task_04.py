# Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

list01 = [1, 8, 5, 7, 12, 25, 4, 8, 12]


for item in list01:
    if list01.count(item) > 1:
        for i in range(list01.count(item)):
            list01.remove(item)
print(list01)