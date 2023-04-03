"""Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
шестизначный идентификационный номер
уровень доступа вычисляемый как остаток от деления суммы цифр id на семь"""


class Human:

    def __init__(self, name: str, age: int, phone: int, mail: str) -> None:
        self.name = name
        self.__age = age
        self.phone = phone
        self.mail = mail

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return self.name

    def info(self):
        a = (f'Phone number is: {self.phone}, mail is: {self.mail}')
        return a

    def get_age(self):
        return self.__age


class Colleague(Human):
    def __init__(self, name: str, age: int, phone: int, mail: str, id : int) -> None:
        super().__init__(name, age, phone, mail)
        self.id = id
        self.level = None
    def acsess(self):
        tmp = 0
        for i in str(self.id):
            tmp += int(i)
        self.level = tmp % 7


id_p = Colleague("Pol", 25, 321654, 'pol@mail.ru', 100258789)

