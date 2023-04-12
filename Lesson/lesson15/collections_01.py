"""Модуль collections"""

# from collections import namedtuple
# from datetime import datetime
#
# User = namedtuple('User', ['first_name', 'last_name','birthday'])
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
# print(u_1)
#
# print(f'{type(User)}, {type(u_1)}')


"""доступ к свойствам используя точечную нотацию."""
#
# from collections import namedtuple
# from datetime import datetime
#
# User = namedtuple('User', ['first_name', 'last_name', 'birthday'])
# u_1 = User('Исаак', 'Ньютон', datetime(1643, 1, 4))
# print(u_1)
# print(u_1.first_name, u_1.birthday.year)


"""При создании класса можно дополнительно передать список значений по
умолчанию. И если дефолтных значений меньше, чем свойств в классе, назначение
происходит справа налево"""

# import time
# from collections import namedtuple
# from datetime import datetime
#
# User = namedtuple('User', ['first_name', 'last_name',
#                            'birthday'], defaults=['Иванов', datetime.now()])
# u_1 = User('Исаак')
# print(f'{u_1.last_name}, {u_1.birthday.strftime("%H:%M:%S")}')
# time.sleep(7)
# u_2 = User('Галилей', 'Галилео')
# print(f'{u_2.last_name}, {u_2.birthday.strftime("%H:%M:%S")}')


"""Как и в случае с неизменяемыми датами, экземпляры namedtuple также неизменны.
Но если надо внести правку в какое-то поле, встроенный метод _replace создаст
копию, заменив только указанные значения."""
#
# from collections import namedtuple
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# a = Point(2, 3, 4)
# b = a._replace(z=0, x=a.x + 4)
# print(b)

"""Экземпляры можно сортировать. Метод проверки “меньше” определяется для
свойств автоматически"""
# from collections import namedtuple
#
# Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
# data = [Point(2, 3, 4), Point(10, -100, -500), Point(3, 7, 11),
#         Point(2, 202, 1)]
# print(sorted(data))


"""Если все свойства являются
объектами неизменяемого типа, экземпляр может быть ключом словаря, элементом
множества и т.п."""
from collections import namedtuple

Point = namedtuple('Point', 'x y z', defaults=[0, 0, 0])
d = {
    Point(2, 3, 4): 'first',
    Point(10, -100, -500): 'second',
    Point(3, 7, 11): 'last',
}
print(d)
mut_point = Point(2, [3, 4, 5], 6)
print(mut_point)
# d.update({mut_point: 'bad_point'})  # TypeError: unhashable type:'list'
