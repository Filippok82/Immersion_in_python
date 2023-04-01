"""4. Декоратор @property и доступ к свойству"""

# class User:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#
# user = User('Стивен')
# print(f'{user.name = }')
# # user.name = 'Славик'  # AttributeError: can't set attribute 'name'

"""Getter
Декоратор property позволяет создавать “геттеры”. Это методы, которые выдают
себя за свойства, позволяют прочитать результат, но блокируют возможность
записи. """

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# user = User('Стивен', 'Спилберг')
# print(f'{user.first_name = }\n{user.last_name =}\n {user.full_name =}')
# # user.full_name = 'Стивен Хокинг'  # AttributeError: can't set attribute 'full_name'
# user.last_name = 'Хокинг'
# print(f'{user.first_name = }\n{user.last_name =}\n{user.full_name =}')


"""● Setter
Python позволяет к “геттеру” добавить “сеттер” — метод контролирующий
изменение свойства."""

# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#
#         else:
#             raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
#
#
# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошёл один год.')
# user.age = 76
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло несколько лет. Изобретена технология омоложения. Но возраст она не уменьшает.')
# user.age = 25  # ValueError: Новый возраст должен быть больше текущего: 76

"""● Deleter
Помимо “геттера” и “сеттера” можно создать “делейтер”. Он выполняется при
вызове команды del для свойства. """

#
# class User:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self._age = 0
#
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, value):
#         if value > self._age:
#             self._age = value
#         else:
#             raise ValueError(f'Новый возраст должен быть больше текущего: {self._age}')
#
#     @age.deleter
#     def age(self):
#         self._age = 0
#
#
# user = User('Стивен', 'Спилберг')
# user.age = 75
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')
# print('Прошло много лет. Изобретена технология перерождения.')
# del user.age
# print(f'Меня зовут {user.full_name} и мне {user.age} лет.')


"""Антипаттерн геттера, сеттера, делейтера"""

"""ПЛОХО"""


class BadPattern:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


"""ХОРОШО"""


class GoodPattern:
    def __init__(self, x):
        self.x = x
