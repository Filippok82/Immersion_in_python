"""2. Инкапсуляция
В ряде языков программирования под инкапсуляцией понимается сокрытие части
свойств и методов класса от доступа извне класса.

Модификаторы доступа
В классическом ООП выделяют следующие модификаторы доступа:
● public — публичный доступ, т.е. возможность обратиться к свойству или
методу из любого другого класса и экземпляра
● protected — защищённый доступ, позволяющий обращаться к свойствам и
методам из класса и из классов наследников.
● private — приватный доступ, т.е. отсутсвие возмодности обратиться к свойству
или методы из другого класса или экземпляра.
В Python по умолчанию все свойства и методы публичные. Однако существуют
соглашения по стилю имён, которые делают атрибуты защищёнными/приватным.
Речь в очередной раз пойдёт о символе подчеркивания.
"""
# Одно подчёркивание в начале защищенный доступ

# class Person:
#     max_up = 3
#     _max_level = 80
#
#     def __init__(self, name, race='unknown', speed=100):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#         self._speed = speed
#
#     def _check_level(self):
#         return self.level < self._max_level # можно из защищенного метода к защищенному атрибуту
#
#     def level_up(self):
#         if self._check_level():
#             self.level += 1
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
# p1 = Person('Сильвана', 'Эльф', 120)
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу', speed=60)
# print(f'{p1._max_level = }')
# print(f'{p2._speed = }')
# p2._speed = 150
# print(f'{p2._speed = }')
# p3.level_up()
# print(f'{p3.level = }')
# p3.level = 80
# p3.level_up()
# print(f'{p3.level = }')


# Два подчёркивания в начале приватный доступ

class Person:

    __max_up = 3
    _max_level = 80

    def __init__(self, name, race='unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed
        self.up = 3

    def _check_level(self):
        return self.level < self._max_level

    def level_up(self):
        if self._check_level():
            self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity

    def add_up(self):
        self.up += 1
        self.up = min(self.up, self.__max_up)


p1 = Person('Сильвана', 'Эльф', 120)
print(f'{p1.up = }')
p1.up = 1
print(f'{p1.up = }')
for _ in range(5):
    p1.add_up()
print(f'{p1.up = }')
# print(p1.__max_up) # AttributeError: 'Person' object has no attribute '__max_up'
# print(Person.__max_up) # AttributeError: type object 'Person' has no attribute '__max_up'
print(p1._Person__max_up)
print(Person._Person__max_up)