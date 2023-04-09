"""Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
"""
import csv
import os.path


class Journal:
    def __init__(self, name):
        self.name = name
        self.file_name = None
        self.my_list = [[]]

    @property
    def validate(self):

        if not self.name.isalpha():
            print(f'Значение {self.name} должно содержать только буквы')

        elif not self.name.istitle():
            print(f'Значение {self.name} должно начинаться с заглавной буквы')

        else:
            file_name = f'{self.name}.csv'
            return file_name

    def read_csv(self):
        file = f'{self.name}.csv'
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as r_csv:
                self.my_list = list(csv.reader(r_csv))
            return self.my_list
        else:
            print(f'нет такого студента {file}')


class Student:

    def __init__(self, name):
        self.name = name
        self.lessons = []
        self.estimation = []
        self.aver_estimation = int
        self.marks = 0
        self.aver_marks = int

    def lesson(self):
        with open(f'{self.name}.csv', 'r', encoding='utf-8') as r_csv:
            self.lessons = list(csv.reader(r_csv))

        for item in self.lessons:
            for i in item[1]:
                if i.isnumeric():
                    self.estimation.append(int(i))
                    self.aver_estimation = sum(self.estimation) / len(self.estimation)
        print(f'Средняя оценка студента {self.name} по всем предметам {self.aver_estimation} ')

        for line in self.lessons:
            num = line[2].split(',')
            self.marks = 0
            for item in num:
                temp = int(item)
                self.marks += int(temp)
            self.aver_marks = self.marks / len(num)
            return f'Средний балл по тестам по предмету {line[0]}  -  {self.aver_marks}'


if __name__ == '__main__':
    j = Journal('Ivanov')
    s = Student('Ivanov')
    print(j.validate)
    print(j.read_csv())
    print(s.lesson())
    # j1 = Journal('petrov123')
    # print(j1.validate)
    # print(j1.read_csv())