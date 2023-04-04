"""Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания
(time.time)"""
import time


class MyString(str):
    """Комментарий к классу"""

    def __new__(cls, value: str, author: str):
        """Комментарий к параметру"""
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'Экземпляр класса с именем автора{self.author}'


if __name__ == '__main__':
    s = MyString("jdfosdfiosdfis", "Tryry")
    print(s)
    print(s.time)
    print(s.author)
    # help(MyString)
    help(s)

print(f'Документация класса: {MyString.__doc__ = }')
print(f'Документация экземпляра: {s.__new__.__doc__ = }')
