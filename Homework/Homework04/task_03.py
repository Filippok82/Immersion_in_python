"""Задачу о банкомате
Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег"""

MAX_SUM = 5000000
SUM_WALLET = []
ANSWER = str


def user_interface():
    select = input('Введите 1 внесения наличных, введите 2 для снятия наличных:')
    if select == '1':
        return initial_fun()
    elif select == '2':
        withdraw_money()
    elif select == '3':
        print("Спасибо, что воспользовались нашими услугами")
        exit()

def initial_fun(m):
    if int(m) % 50 == 0:
        SUM_WALLET.append(int(m))
        print(f'На вашем счете:{sum(SUM_WALLET)}')
        ANSWER = str(input(f"Хотите продолжить операцию да или нет "))

        if ANSWER == "да":
            m = 0
            return initial_fun(m)
        elif ANSWER == "нет":
            initial_fun(m)


def withdraw_money(n: int):
    pass


user_interface()
money = (input("Введите сумму для пополнения 100, 150, 200, 250, 300:"))
initial_fun(money)
