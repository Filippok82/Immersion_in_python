"""3. Представления экземпляра"""

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
# user = User('Спенглер')
# print(user)


"""Представление для пользователя, __str__
Дандер метод __str__ используется для получения удобного пользователю
описания экземпляра."""

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __str__(self):
#         return f'Экземпляр класса User с именем "{self.name}"'
#
#
# user = User('Спенглер')
# print(user)


"""Представление для создания экземпляра,
__repr__"""

# class User:
#     def __init__(self, name: str):
#         """Added the name parameter."""
#         self.name = name
#
#     def simple_method(self):
#         """Example of a simple method."""
#         self.name.capitalize()
#
#     def __repr__(self):
#         return f'User({self.name})'
#
#
# user = User('Спенглер')
# print(user)
# ____________________________________________________________

#
# class User:
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
#
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)


"""Приоритет методов"""
#
# class User:
#
#     def __init__(self, name: str, equipment: list = None):
#         self.name = name
#         self.equipment = equipment if equipment is not None else []
#         self.life = 3
#
#     def __str__(self):
#         eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
#         return f'Перед нами {self.name} с {eq}. Количество жизней- {self.life}'
#
#     def __repr__(self):
#         return f'User({self.name}, {self.equipment})'
#
#
# user = User('Венкман', ['протонный ускоритель', 'ловушка'])
# print(user)
# print(f'{user}')
# print(repr(user))
# print(f'{user = }')
#

"""Печать коллекций"""


class User:
    def __init__(self, name: str, equipment: list = None):
        self.name = name
        self.equipment = equipment if equipment is not None else []
        self.life = 3

    def __str__(self):
        eq = 'оборудованием: ' + ', '.join(self.equipment) if self.equipment else 'пустыми руками'
        return f'Перед нами {self.name} с {eq}. Количество жизней- {self.life}'

    def __repr__(self):
        return f'User({self.name}, {self.equipment})'


u_1 = User('Спенглер')
u_2 = User('Венкман', ['протонный ускоритель', 'ловушка'])
u_3 = User(equipment=['ловушка', 'прибор ночного видения'], name='Стэнц')
ghostbusters = [u_1, u_2, u_3]
print(ghostbusters)
print(f'{ghostbusters}')
print(repr(ghostbusters))
print(f'{ghostbusters = }')
print(*ghostbusters, sep='\n')
