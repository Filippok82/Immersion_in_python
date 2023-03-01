# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

num: int = int(input('Введите число:'))
SIXTEEN = 16

print(hex(num))


res = ''
digit = '0123456789ABCDEF'

while num > 0:
    res = digit[num % SIXTEEN] + res
    num = num // SIXTEEN

print(res)

