"""Создайте функцию, которая запрашивает числовые данные от
пользователя до тех пор, пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения."""


# def task_01(text: str = None) -> int:
#     while True:
#         try:
#             num = int(input(text))
#             break
#         except ValueError as e:
#             print(f'Ошибка ValueError: {e}\n' f'Попробуйте снова')
#             try:
#                 num = float(input(text))
#                 break
#             except ValueError as e:
#                 print(f'Ошибка ValueError: {e}\n' f'Попробуйте снова')
#     return num
#
#
# if __name__ == '__main__':
#     number = task_01('Введите целое или вещественное число: ')


def get(text: str = None) -> int:
    while True:
        data = input(text)
        try:
            num = float(data)
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
            f'Попробуйте снова')
    return num
if __name__ == '__main__':

    number = get('Введите число: ')
    print(number)