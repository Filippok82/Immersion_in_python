import csv

# field_names = ['Предмет', 'Оценки', 'Баллы']
#
# rows = [
#     {'Предмет': 'математика', 'Оценки': '5,4,4,5', 'Баллы': '65,80,60,85'},
#     {'Предмет': 'русский язык', 'Оценки': '4,5,3,5', 'Баллы': '50,75,85,40'},
#     {'Предмет': 'биология', 'Оценки': '5,5,4,5', 'Баллы': '85,90,95,99'},
# ]
#
# with open('Ivanov.csv', 'w', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
#     writer.writeheader()
#     writer.writerows(rows)

with open('Ivanov.csv', 'w', encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(['математика', '5,4,4,5', '65,80,60,85'])
    file_writer.writerow(['русский язык', '4,5,3,5', '50,75,85,40'])
    file_writer.writerow(['биология', '5,5,4,5', '85,90,95,99'])
