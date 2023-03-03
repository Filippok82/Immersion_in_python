# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

my_tuple = (8, 'dog', True, 44, 8, False, 'cat')

my_dict = {}

for item in my_tuple:
    key = my_dict.setdefault(type(item), list())
    key.append(item)

print(my_dict)