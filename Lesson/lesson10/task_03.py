"""3. Наследование
В Python все объекты являются наследниками класса object. В начале лекции мы
рассмотрели пример создания класса:
class Person:
pass
Представленная запись создания класса является упрощённой. На самом деле
класс Person наследуется от класса object. Т.е. object — родительский класс для
Person, а Person — дочерний класс для object.
class Person(object):
pass """

# class Person:
#     __max_up = 3
#     _max_level = 80
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# print(f'{p1.power = }')
# print(f'{p1.name = }, {p1.up = }, {p1.power = }')


"""Переопределение методов
При наследовании мы можем использовать в дочернем классе все общедоступные
свойства и методы родительского класса. Кроме того можно создать свои. И если
имена будут совпадать, произойдёт переопределение. Будут браться значения
дочернего класса."""

# class Person:
#     __max_up = 3
#     _max_level = 80
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#
#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2
#
#     def add_many_up(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)
#
#
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# p2 = Person('Маг', 'Тролль')
# print(f'{p1.health = }, {p2.health = }')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }')
# p2.change_health(p1, 10)
# print(f'{p1.health = }, {p2.health = }')
# p1.add_many_up()
# print(f'{p1.up = }')


"""Множественное наследование
Python поддерживает множественное наследование. Класс может быть
наследником сразу двух и более классов. В некоторых языках множественное
наследование недоступно по причине усложнения кода. Например наследуя класс
существо от классов птицы и рыбы позволит создать летающую рыбу или
плавающую птицу?"""

# class Person:
#     __max_up = 3
#     _max_level = 80
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#         self.up = 3
#
#     def _check_level(self):
#         return self.level < self._max_level
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
#     def add_up(self):
#         self.up += 1
#         self.up = min(self.up, self.__max_up)
#
#
# class Address:
#
#     def __init__(self, country, city, street):
#         self.country = country or ''
#
#         self.city = city or ''
#         self.street = street or ''
#
#     def say_address(self):
#         return f'Адрес героя: {self.country}, {self.city},{self.street}'
#
#
# class Weapon:
#
#     def __init__(self, left_hand, right_hand):
#         self.left_hand = left_hand or 'Клинок'
#
#         self.right_hand = right_hand or 'Лук'
#
#
# class Hero(Person, Address, Weapon):
#
#     def __init__(self, power, name=None, race=None, speed=None,
#                  country=None, city=None, street=None,
#                  left_hand=None, right_hand=None):
#         self.power = power
#
#
#         Person.__init__(self, name, race, speed)
#         Address.__init__(self, country, city, street)
#         Weapon.__init__(self, left_hand, right_hand)
#
#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2
#
#     def add_many_ups(self):
#         self.up += 1
#         self.up = min(self.up, self._Person__max_up * 2)
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120, country='Эльфляндия', street='Ночного эльфа', left_hand='Стрела')
#
# print(f'{p1.say_address()}')
# print(f'{p1.right_hand = }, {p1.left_hand = }')


"""MRO
Аббревиатура MRO — method resolution order переводится как “порядок разрешения
методов”. Относится этот порядок не только к методам, но и ко всем атрибутам
класса. Это внутренний механизм, определяющий порядок наследования.
"""


class A:

    def __init__(self):
        print('Init class A')
        self.data_a = 'A'

    def say(self):
        print('Текст')
        print(self.data_b)


class B:
    def __init__(self):
        print('Init class B')
        self.data_b = 'B'


class C:
    def __init__(self):
        print('Init class C')
        self.data_c = 'C'


class D:
    def __init__(self):
        print('Init class D')
        self.data_d = 'D'


class X1(A, C):
    def __init__(self):
        print('Init class X1')
        super().__init__()


class X2(B, D):
    def __init__(self):
        print('Init class X2')
        super().__init__()


class X3(A, D):
    def __init__(self):
        print('Init class X3')
        super().__init__()


class Z(X1, X2, X3):
    def __init__(self):
        print('Init class Z')
        super().__init__()


print(*Z.mro(), sep='\n')
z = Z()
print(f'{z.data_b = }')
# print(f'{z.data_a = }') # AttributeError: 'Z' object has no attribute 'data_a'
z = Z()
z.say()

a = A()
# a.say()
