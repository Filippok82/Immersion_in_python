"""Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста
и для пользователя.
"""


class Archive():
    _one = None

    def __init__(self, num: int, val: str) -> None:
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __str__(self):
        return f'Класс записывает число {self.num} и строку {self.val} в словарь'

    def __repr__(self):
        return f'Archive({self.num}, "{self.val}")'


s = Archive(123, '123355')
print(s.numbers, s.values)
s = Archive(5887, 'Hello')
print(s.numbers, s.values)
s = Archive(8952, 'Hi')
print(s.numbers, s.values)
s1 = Archive(4526, 'DOGS')
print(f'{s1.num}, {s1.val}')
