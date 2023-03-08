"""Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии"""


def my_func05(names: list[str], level: list[int], bonus: list[str]) -> dict[str, int, float]:
    my_dict = {}
    for n, l, b in zip(names, level, bonus):
        my_dict[n] = l * float(b[:-1])/100
    return my_dict



list01 = ['Mark', 'Nik', 'Alex']
list02 = [25000, 45000, 32000]
list03 = ['15.5%', '25.8%', '10.3%']
print(my_func05(list01, list02, list03))
