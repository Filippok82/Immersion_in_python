"""Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст"""


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


p1 = Human('Ivan', 25, 123456, 'ivan@mail.ru')
print(p1.get_age(), p1.info())
p1.birthday()
print(p1.get_age(), p1.info())