"""1. Обработка исключительных
ситуаций в Python"""

# def get(text: str = None) -> int:
#     data = input(text)
#     num = int(data)
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
# print(f'100 / {number} = {100 / number}')
from random import randint

"""Команда try"""

#
# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


"""Команда except
"""

# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#         num = 1
#         print(f'Будем считать результатом ввода число {num}')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')


"""Цикл while для обработки ошибок ввода
"""

#
# def get(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n' f'Попробуйте снова')
#     return num
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
# print(f'100 / {number} = {100 / number}')

# _________________________________________________________

# MAX_COUNT = 5
#
#
# def get_data():
#     """Получает данные из внешнего источноика."""
#     if result := randint(0, 3):
#         return result
#     else:
#         raise ConnectionError
#
#
# count = 0
# while count < MAX_COUNT:
#     count += 1
#     try:
#         data = get_data()
#         break
#     except ConnectionError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#
# print((data))


"""Несколько except для одного try.
"""

# def hundred_div_num(text: str = None) -> tuple[int, float]:
#     while True:
#         try:
#             num = int(input(text))
#             div = 100 / num
#             break
#         except ValueError as e:
#             print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
#                   f'Попробуйте снова')
#         except ZeroDivisionError as e:
#             div = float('inf')
#             break
#     return num, div
#
#
# if __name__ == '__main__':
#     n, d = hundred_div_num('Введите целый делитель: ')
#     print(f'Результат операции: "100 / {n} = {d}"')

"""Команда else
"""

# MAX_COUNT = 5
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         result = 100 / num
#         break
# print(f'{result = }')


# _________________________________________________________
"""Вложенные блоки обработки исключений"""

# MAX_COUNT = 5
#
# result = None
# for count in range(1, MAX_COUNT + 1):
#     try:
#         num = int(input('Введите целое число: '))
#         print('Успешно получили целое число')
#     except ValueError as e:
#         print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
#     else:
#         try:
#             result = 100 / num
#         except ZeroDivisionError as e:
#             result = float('inf')
#         break
# print(f'{result = }')

"""Команда finally
"""

#
# def get(text: str = None) -> int:
#     num = None
#     try:
#         num = int(input(text))
#     except ValueError as e:
#         print(f'Ваш ввод привёл к ошибке ValueError: {e}')
#     finally:
#         return num if isinstance(num, int) else 1
#
#
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     try:
#         print(f'100 / {number} = {100 / number}')
#     except ZeroDivisionError as e:
#         print(f'На ноль делить нельзя. Получим {e}')


"""Блок finally без except"""

file = open('text.txt', 'r', encoding='utf-8')
try:
    data = file.read().split()
    print(data[len(data)])
finally:
    print('Закрываю файл')
    file.close()
