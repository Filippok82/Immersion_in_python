"""Создайте класс-функцию, который считает факториал числа при
вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и
их факториалов."""


class Factorial:
    def __init__(self, k: int):
        self.k = k
        self.val_list = [None] * self.k
        self.key_list = [None] * self.k

    def __call__(self, n: int, *args, **kwds):
        if (n == 1 or n == 0):
            return 1
        result = 1
        for i in range(1, n + 1):
            result = i * result
        self.val_list.append(result)
        self.val_list.pop(0)
        self.key_list.append(n)
        self.key_list.pop(0)
        # print(self.val_list, self.key_list)
        return result

    def view(self):
        return f'{self.val_list} \n {self.key_list}'


f = Factorial(5)
print(f(6))
print(f(7))
print(f(8))
print(f(5))
print(f(4))
print(f(3))
print(f.view())