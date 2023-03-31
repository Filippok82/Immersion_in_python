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


if __name__ == '__main__':
    s = MyString("jdfosdfiosdfis", "Tryry")
    print(s)
    print(s.time)
    print(s.author)
    # help(MyString)
    help(s)

