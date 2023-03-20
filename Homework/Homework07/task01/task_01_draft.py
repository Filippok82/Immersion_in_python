"""Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
 Далее счётчик файлов и расширение. """

# import os
# from random import randint
#
# def group_renaming(dn: str, cn: int):
#     file_num = [randint(1, 10) for _ in range(cn)]
#     file_num01 = ''.join(map(str, file_num))
#     name_file = ''
#     name_file += dn + file_num01
#     print(name_file)
#
#     for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#         print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
#         for i in file_name:
#             split_tup = os.path.splitext(i)
#             print(f'расширение и имя файла {split_tup}')
#             file_extension = split_tup[1]
#             print(file_extension)
#             if '.txt' in file_extension:
#                 name_file += file_extension
#                 print(name_file)
#                 for i in file_name:
#                     os.rename(i, name_file)
#
#
#
# desired_name = input('Введите желаемое имя: ')
# count_num = int(input('Количество цифр в порядковом номере:'))
#
# group_renaming(desired_name, count_num)



