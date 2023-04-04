"""Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
list-архивы также являются свойствами экземпляра
"""


class Archive():
    """Комментарий к классу."""
    _one = None

    def __init__(self, num: int, val: str) -> None:
        """Комментарий к параметрам."""
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        """Комментарий к методу. """
        if cls._one is None:
            cls._one = super().__new__(cls)
            cls._one.numbers = []
            cls._one.values = []
        else:
            cls._one.numbers.append(cls._one.num)
            cls._one.values.append(cls._one.val)
        return cls._one

    def __repr__(self):
        return f'Archive {self.val}  {self.num}'


if __name__ == '__main__':
    s = Archive(123, '123355')
    print(s)
    print(s.numbers, s.values)

    s = Archive(5887, 'Hello')
    print(s.numbers, s.values)

    s = Archive(8952, 'Hi')
    print(s.numbers, s.values)

    print(f'Документация класса: {Archive.__doc__ = }')
    print(f'Документация экземпляра: {s.__new__.__doc__ = }')
