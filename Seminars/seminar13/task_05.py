"""Доработаем задачи 3 и 4. Создайте класс проекта, который
имеет следующие методы:
загрузка данных (функция из задания 4)
вход в систему - требует указать имя и id пользователя. Для
проверки наличия пользователя в множестве используйте
магический метод проверки на равенство пользователей.
Если такого пользователя нет, вызывайте исключение
доступа. А если пользователь есть, получите его уровень из
множества пользователей.
добавление пользователя. Если уровень пользователя
меньше, чем ваш уровень, вызывайте исключение уровня
доступа.
"""

import json

from task_03 import LevelError, AccessError


class User:
    def __init__(self, name: str, user_id: int, level: int):
        self.name = name
        self.user_id = id
        self.level = level

    def __eq__(self, other) -> bool:
        return self.user_id == other.user_id and self.name == other.name


class Project:
    def __init__(self) -> None:
        self.level = None
        self.users = set()
        self.user = None

    def reed_json(self, file_name: str):

        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for level, value in data.items():
            for user_id, name in value.items():
                self.users.add(User(name=name, user_id=int(user_id), level=int(level)))
        return self.users

    def enter(self, name: str, user_id: int):
        u = User(name=name, user_id=user_id, level=0)

        if u not in self.users:
            raise AccessError

        for item in self.users:
            if u == item:
                self.user = item
                return self.user

    def add_user(self, name, user_id, level):

        u = User(name=name, user_id=user_id, level=level)

        for item in self.users:
            if u < item:
                raise LevelError
        else:
            return self.users


if __name__ == '__main__':
    u1 = User('Fockus', 2, 0)
    p1 = Project()
    print(p1.reed_json('ident.json'))
    # print(p1.enter('Miron', 2))
    # print(p1.add_user())
