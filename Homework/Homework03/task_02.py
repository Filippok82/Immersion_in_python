# Дан список повторяющихся элементов. Вернуть список
# с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.

list01 = [1, 2, 22, 55, 55, 45, 55, 55, 32, 14, 22, 2, 2, 1]
print(list01)
list02 = []
for item in list01:
    if list01.count(item) > 1:
        list02.append(item)
    for i in list02:
        if list02.count(i) > 1:
            list02.remove(i)
print(list02)
