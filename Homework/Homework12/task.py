import csv


class Students:

    def __init__(self, name, age, subject, office):
        self.name = name
        self.age = age
        self.subject = subject
        self.office = office

    def __repr__(self):
        return f'Student(Имя = {self.name}, Возраст = {self.age}, Предметы = {self.subject}, Кабинет = {self.office})'

    def readingCsv(self):
        numberList = []
        with open('subjects.csv', 'r', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                numberList.append(line)
            return numberList


if __name__ == '__main__':
    s = Students("Иванов Иван Иванович", 18, "subjects", 32)
    subjects = s.readingCsv()
    s.subject = subjects
    print(s.__repr__())