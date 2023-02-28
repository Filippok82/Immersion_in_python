# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

num: int = int(input('Введите число:'))
DOUBLE = 2
OCT = 8

print(bin(num))
print(oct(num))

number = num
for i in DOUBLE, OCT:
    num = number
    result = ''
    while num > 0:
        double_num = num % i
        result = str(double_num) + result
        num = num // i
    print(result)


#
# while number > 0:
#     double_num = number % 8
#     res =  str(double_num) + res
#     number = number // 8
# print(res)