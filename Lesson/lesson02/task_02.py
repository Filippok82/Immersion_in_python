# Аннотация типов
#
# a: float = 42.0
# b: float = float(input('Введи число: '))
# a = a / b

#____________________________________________________

# def my_func(data: list[int, float]) -> float:
#     res = sum(data) / len(data)
#     return res
# print(my_func([2, 5.5, 15, 8.0, 13.74]))

# ________________________________________________________
a: int | float = 42
b: float = float(input('Введи число: '))
a = a / b
