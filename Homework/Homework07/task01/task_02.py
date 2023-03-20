"""Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени.
Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано.
 Далее счётчик файлов и расширение. """

import os

__all__ = ['group_renaming', 'count_num','desired_name', 'file_extension']


def group_renaming(cn: int, dn: str, fe: str):

    count = f'{{0:0{cn}d}}'
    # print(count)
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        for i, f in enumerate(file_name):
            if fe in f:
                f_name, f_ext = os.path.splitext(f)
                name = '{}'.format(f_name[2:7]) + dn + count.format(i) + f_ext
                os.rename(f, name)
                print(name)


count_num = int(input("Сколько цифр в порядковом номере: "))
desired_name = input('Введите желаемое имя: ')
file_extension = '.txt'
print(group_renaming(count_num, desired_name, file_extension))
