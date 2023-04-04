"""Создайте класс-генератор.
Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
Если переданы два параметра, считаем step=1.
Если передан один параметр, также считаем start=1."""

class MyFac:
    def __init__(self, *args):
        match len(args):
            case 1:
                self.start = 1
                self.stop = args[0]
                self.step = 1
            case 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            case 3:
                self.start = args[0]
                self.stop = args[1]
                self.step = args[2]

    def __iter__(self):
        return self

    def __next__(self):
        # if(self.start==1 or self.stop==0):
        #      return 1
        while self.start < self.stop:
            result = 1
            for i in range(2, self.start + 1):
                result = i * result
            self.start += self.step
            return result
        raise StopIteration


fib = MyFac(0, 8, 1)
for num in fib:
    print(num)

# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())
# print(fib.__next__())