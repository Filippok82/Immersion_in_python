# Задача №8
# Нарисовать в консоли ёлку спросив у пользователя количество
# рядов.


a = ' '
n = int(input('Сколько рядов будет у елки:'))
for i in range(0, n + 1):
    print(a * (n - i) + '*' * (i * 2 - 1))




