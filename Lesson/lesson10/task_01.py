"""1. Основы ООП в Python
Классы"""

# data = list((1, 2, 3))
# print(f'{data = }, {type(data) = }, {type(list) = }')

# __________________________________________________________
#
# import random
# import supermodule
#
# result1 = random.randint(1, 10)
# result2 = supermodule.randint(42)
# print(result1)
# print(result2)

# ____________________________________

# class Person:
#     max_up = 3 # атрибут класса
#
#
# p1 = Person()  # экземпляр класса
# print(f'{p1.max_up=}')
#
# print(f'{Person.max_up=}')

# ________________________________________________________

"""Атрибуты класса и экземпляров
Переменная max_up в классе считается атрибутом класса. В некоторой литературе
такие переменные называют свойствами класса. Также иногда используют термин
поля класса. Свойства позволяют хранить значения и переходят ко всем
экземплярам класса"""

# class Person:
#
#     max_up = 3
#
# p1 = Person()
# p2 = Person()
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
#
# p1.max_up = 12
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')
#
# Person.max_up = 42
# print(f'{Person.max_up = }, {p1.max_up = }, {p2.max_up = }')


"""Динамическая структура класса
Класс и экземпляр являются динамическими объектами. Мы можем добавлять
атрибуты в процессе работы, а не только в момент создания класса."""

# class Person:
#     max_up = 3
#
#
# p1 = Person()
# p2 = Person()
# Person.level = 1
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')
#
# p1.health = 100
# # print(f'{Person.health = }, {p1.health = }, {p2.health = }')  # AttributeError: type object 'Person' has no attribute 'health'
# # print(f'{p1.health = }, {p2.health = }')  # AttributeError: 'Person' object has no attribute 'health'
# print(f'{p1.health = }')


# _______________________________________________


# class Person:
#
#     pass
#
# p1 = Person()
# p1.level = 1
# p1.health = 100
#
# dict_p1 = {}
# dict_p1['level'] = 1
# dict_p1['health'] = 100
#
# print(f'{p1.health = }')
# print(f'{dict_p1["health"] = }')


"""Конструктор экземпляра
При создании класса обычно используют функцию конструктор __init__."""

#
# class Person:
#
#     max_up = 3
#
#     def __init__(self):
#
#         self.level = 1
#         self.health = 100
# p1 = Person()
# p2 = Person()
# print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
# print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# # print(f'{Person.max_up = }, {Person.level = }, {Person.health =}') # AttributeError: type object 'Person' has no attribute 'level'
# Person.level = 100
# print(f'{Person.level = }, {p1.level = }, {p2.level = }')


"""Передача аргументов в экземпляр
При создании экземпляра можно передать значения в конструктор и тем самым
добавить свойства, характерные для конкретного экземпляра."""
# class Person:
#     max_up = 3
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.name = }, {p1.race = }')
# print(f'{p2.name = }, {p2.race = }')
#
# print(f'{p3.name = }, {p3.race = }')

"""Методы класса
Функция внутри класса называется методом. Мы уже рассмотрели магический
метод __init__, который вызывается при создании экземпляра класса. Помимо этого
можно создавать любые методы внутри класса и обращаться к ним из экземпляра
через точечную нотацию. Различие между обращением к свойству и к методу -
круглые скобки после имени."""

# class Person:
#     max_up = 3
#
#     def __init__(self, name, race='unknown'):
#         self.name = name
#         self.race = race
#         self.level = 1
#         self.health = 100
#
#     def level_up(self):
#         self.level += 1
#
#
# p1 = Person('Сильвана', 'Эльф')
# p2 = Person('Иван', 'Человек')
# p3 = Person('Грогу')
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')
# p3.level_up()
# p1.level_up()
# p3.level_up()
# print(f'{p1.level = }, {p2.level = }, {p3.level = }')

"""При желании можно передавать в метод аргументы. И так как в Python всё объект,
можно передать даже экземпляр класса."""

class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

    def level_up(self):
        self.level += 1

    def change_health(self, other, quantity):
        self.health += quantity
        other.health -= quantity


p1 = Person('Сильвана', 'Эльф')
p2 = Person('Иван', 'Человек')
p3 = Person('Грогу')
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
p1.change_health(p2, 10)
print(f'{p1.health = }, {p2.health = }, {p3.health = }')
