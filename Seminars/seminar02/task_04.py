# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 42

diametr = decimal.Decimal(input('Введите диаметр: '))
pi = decimal.Decimal(math.pi)
MAX_LIMIT = 1000
if diametr <= MAX_LIMIT:
    lenght = pi * diametr
    square = pi * (diametr / 2) ** 2
    print(lenght, square)
else:
    print('Число слишком большое')
