"""Задание №6
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег"""

# class Bancomat:
#     def __init__(self, money, wallet):
#         self.money = money
#         self.wallet = wallet
#
#     def remove(self, money):
#
#         self.wallet =
#     def insert(self):
#     def exit(self):

global wallet
MON = int





def remove_money(wallet: int):
    print(f' у вас {wallet} ')
    m = int(input(f"Введите сумму для снятия "))
    if wallet > m:

        if m % 50 == 0:
            wallet -= m
    else:
        print(f'У вас {wallet}')



def insert():
    pass


def exit_seans():
    print('Приходите еще')


button = int(input(f'Нажмите 1 для снятия 2 для пополнения 3 для выхода '))
if button == 1:
    remove_money(wallet=0)
elif button == 2:
    insert()
else:
    exit_seans()
