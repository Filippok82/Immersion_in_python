"""6. Обработка атрибутов"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#
# a = Vector(2, 4)


"""Получение значения атрибута,
__getattribute__"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#
# a = Vector(2, 4)
# # print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')


"""Присвоение атрибуту значения, __setattr__"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#
#
# a = Vector(2, 4)
# # print(a.z)  # AttributeError: У нас вектор на плоскости, а не в пространстве
# print(f'{a = }')
# # a.z = 73  # AttributeError: У нас вектор на плоскости, а не в пространстве
# a.x = 3
# print(f'{a = }')


"""Обращение к несуществующему атрибуту,
__getattr__
"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Vector({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __getattribute__(self, item):
#         if item == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('У нас вектор на плоскости, а не в пространстве')
#         return object.__setattr__(self, key, value)
#
#     def __getattr__(self, item):
#         return None
#
#
# a = Vector(2, 4)
# print(a.z)  # None
# print(f'{a = }')


"""Удаление атрибута, __delattr__"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __getattribute__(self, item):
        if item == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'z':
            raise AttributeError('У нас вектор на плоскости, а не в пространстве')
        return object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return None

    def __delattr__(self, item):
        if item in ('x', 'y'):
            setattr(self, item, 0)
        else:
            object.__delattr__(self, item)


a = Vector(2, 4)
a.s = 73
print(f'{a = }, {a.s = }')
del a.x
del a.s
print(f'{a = }, {a.s = }')
