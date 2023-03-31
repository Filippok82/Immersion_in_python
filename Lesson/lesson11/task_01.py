"""Создание экземпляра класса, __init__
"""

# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#     # принтим только в учебных целях, а не для реальных задач
#         print(f'Создал {self} со свойствами:\n'
#         f'{self.name = },\t{self.equipment = },\t{self.life = }')
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print('Создаём третий раз')
# u_3 = User(equipment=['ловушка', 'прибор ночного видения'],name='Стэнц')


"""Контроль создания класса через __new__"""

# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls)
#         print(f'Создал класс {cls}')
#
#         return instance
#
# print('Создаём первый раз')
# u_1 = User('Спенглер')
# print('Создаём второй раз')
# u_2 = User('Венкман')
# print('Создаём третий раз')
# u_3 = User(name='Стэнц')


"""Расширение неизменяемых классов"""

# class NamedInt(int):
#     def __new__(cls, value, name):
#         instance = super().__new__(cls, value)
#         instance.name = name
#         print(f'Создал класс {cls}')
#         return instance
#
#
# print('Создаём первый раз')
# a = NamedInt(42, 'Главный ответ жизни, Вселенной и вообще')
# print('Создаём второй раз')
# b = NamedInt(73, 'Лучшее просто число')
# print(f'{a = }\t{a.name = }\t{type(a) = }')
# print(f'{b = }\t{b.name = }\t{type(b) = }')
# c = a + b
# print(f'{c = }\t{type(c) = }')

"""Шаблон Одиночка, Singleton"""

# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#     def __init__(self, name: str):
#         self.name = name
#
#
# a = Singleton('Первый')
# print(f'{a.name = }')
# b = Singleton('Второй')
# print(f'{a is b = }')
# print(f'{a.name = }\n{b.name = }')

"""Удаление экземпляра класса, __del__"""


# class User:
#     def __init__(self, name: str):
#         self.name = name
#         print(f'Создал {self.name = }')
#
#     def __del__(self):
#         print(f'Удаление экземпляра {self.name}')
#
#
# u_1 = User('Спенглер')
# u_2 = User('Венкман')

"""Команда del"""

import sys


class User:
    def __init__(self, name: str):
        self.name = name
        print(f'Создал {self.name = }')

    def __del__(self):
        print(f'Удаление экземпляра {self.name}')


u_1 = User('Спенглер')
print(sys.getrefcount(u_1))
u_2 = u_1
print(sys.getrefcount(u_1), sys.getrefcount(u_2))
del u_1
print(sys.getrefcount(u_2))
print('Завершение работы')