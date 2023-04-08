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
from task_03 import UserException,LevelError, AccessError




class User:
    def __init__(self, name: str, id: int, level: int):
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, other) -> bool:
        return self.id == other.id and self.name == other.name


class Project:
    def __init__(self) -> None:
        self.users = set()
        self.user = None

    def reed_json(self, file_name: str):

        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for level, value in data.items():
            for id, name in value.items():
                self.users.add(User(name=name, id=int(id), level=int(level)))
        return self.users

    # print(reed_json('ident.json'))
    def enter(self, name: str, id: int):
        u1 = User(name=name, id=id, level=0)

        if u1 not in self.users:
            raise AccessError

        for item in self.users:
            if u1 == item:
                self.user = item
                return self.user

    def add_user():
        pass