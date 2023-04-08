"""Создайте класс с базовым исключением и дочерние классы-исключения:
ошибка уровня,
ошибка доступа."""

class UserException(Exception):
    pass


class LevelError(UserException):
    # pass
    def __str__(self):
        print('ошибка уровня')


class AccessError(UserException):
    # pass
    def __str__(self):
        print('ошибка доступа')