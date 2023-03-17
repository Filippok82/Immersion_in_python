"""Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. Весь период (1 января 1 года
- 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию."""

import datetime


def checking_date(data_in: str) -> bool:
    day, month, year = data_in.split('.')
    try:
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    date = input("Введите дату формате DD.MM.YYYY: ")
    print(checking_date(date))
