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


class Journal:
    def __init__(self, name):
        self.name = name
        self.file = str
        self.my_list = [[]]

    def validate(self):
        global file
        for char in self.name:
            if char.isalpha or char.istitle:
                file = f'{self.name}.csv'
            else:
                print('Проверка имени не пройдена')
            return file

    def read_csv(self):
        with open(file, 'r', encoding='utf-8') as r_csv:
            self.my_list = list(csv.reader(r_csv))
        return self.my_list


# class Student:
#
#     def __init__(self, name):
#         self.name = name
#         self.my_list = Journal.read_csv
#
#     def lesson(self):
#         res = []
#         for item in self.my_list:
#             par_sum = 0
#             print(item)
# for ele in sub:
#     ele = int(ele)
#     t = [[int(v) if v.isnumeric() else v for v in x] for x in ele]
#     res.append(ele)
#
#     print(res)


#             #     par_sum = par_sum + int(ele)
#             # res.append(par_sum)
#             # print(res)

# les1, les2, les3 = my_list
# print(les1)
# for item in les1:
#     print(item)
#     self.marks.append(item[0])
#     print(self.marks)

# l.append(re.findall(i))
# print(l)

# t = [[int(v) if v.isnumeric() else v for v in x] for x in my_list]
#         self.les.append(i)
# print(sum(self.les))
#     self.les.append(elem)
# return self.les
# print(item[0])
# for i in item[1]:
#     lst = item.
#     length = int(len(i))
#     self.marks = sum(i)
# return self.marks
# sub1_avg = sum(n for _, n, _ in l) / float(len(l))
#         sub2_avg = sum(n for  n in item) / float(len(item))
# student_avgs = [{x[0]: sum(x[1:]) // float((len(x) - 1))} for x in l]
#         print (sub2_avg)
# self.les = [sum(int(i)) for i in my_list]
# print(list(map(sum, my_list)))
# for line in range(len(my_list)):
#     self.les.append(l for l in line)
#
#     return self.les


# def __add__(self, S):
#     temp = Student(S.name, [])
#     for i in range(len(self.marks)):
#         temp.marks.append(self.marks[i] + S.marks[i])
#     return temp



if __name__ == '__main__':
    # s = Student('Ivanov')
    # s2 = Student('petro1')
    j = Journal('Ivanov')

    # j1 = Journal('petov4')
    # print(s.lesson())

    print(j.validate())
    print(j.read_csv())
