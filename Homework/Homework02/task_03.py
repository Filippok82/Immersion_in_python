# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем. Программа должна возвращать
# сумму и произведение* дробей. Для проверки своего кода используйте
# модуль fractions.

import fractions
import math

num1 = str(input('Первое число:'))
num2 = str(input('Второе число:'))

a = fractions.Fraction(num1)
b = fractions.Fraction(num2)
print('Проверка:')
print(a, '+', b, '=', a + b)
print(a, '*', b, '=', a * b)

num1 = num1.split('/')
num2 = num2.split('/')
a1 = int(num1[0])
b1 = int(num1[1])
a2 = int(num2[0])
b2 = int(num2[1])

print('Ответ:')
if b1 == b2:
    print('{}/{}'.format(a1 + a2, b1))
else:
    numerator = (a1 * b2 + a2 * b1)
    denominator = (math.lcm(b1, b2))
    n = numerator
    d = denominator
    while n != 0 and d != 0:
        if n >= d:
            n %= d
        else:
            d %= n
    nod = d + n
    print('{}/{}'.format(numerator//nod, denominator//nod))

print('{}/{}'.format(a1 * a2, b1 * b2))
