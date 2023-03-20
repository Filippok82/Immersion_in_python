# Формат CSV

# import csv
#
# with open('biostats.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f)
#     for line in csv_file:
#         print(line)
#     print(type(line))

# __________________________________________________

# import csv
#
#
# with open('biostats_tab.csv', 'r', newline='') as f:
#     csv_file = csv.reader(f, dialect='excel-tab',quoting=csv.QUOTE_NONNUMERIC)
#     for line in csv_file:
#         print(line)
#     print(type(line))

# Запись CSV

# import csv
#
# with open('biostats_tab.csv', 'r', newline='') as f_read, \
#         open('new_biostats.csv', 'w', newline='', encoding='utf-8') as f_write:
#     csv_read = csv.reader(f_read, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
#     csv_write = csv.writer(f_write, dialect='excel', delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     all_data = []
#     for i, line in enumerate(csv_read):
#         if i == 0:
#             csv_write.writerow(line)
#     else:
#         line[2] += 1
#         for j in range(2, 4 + 1):
#             line[j] = int(line[j])
#         all_data.append(line)
#     csv_write.writerows(all_data)

# Запись из словаря

# import csv
# from typing import Iterator
#
#
#
# with open('biostats_tab.csv', 'r', newline='') as f_read, \
#         open('biostats_new.csv', 'w', newline='', encoding='utf-8') as f_write:
#     csv_read: Iterator[dict] = csv.DictReader(f_read, fieldnames=["name", "sex", "age", "height", "weight", "office"],
#                                               restval="Main Office", dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
# csv_write = csv.DictWriter(f_write, fieldnames=["id", "name", "office", "sex", "age", "height", "weight"],
#                            dialect='excel-tab', quoting=csv.QUOTE_ALL)
# csv_write.writeheader()
# all_data = []
# for i, dict_row in enumerate(csv_read):
#     if
# i != 0:
# dict_row['id'] = i
# dict_row['age'] += 1
# all_data.append(dict_row)
# csv_write.writerows(all_data)
