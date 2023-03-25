"""Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки."""

# import json
#
#
# def convert(name: str) -> None:
#     my_dict = {}
#     with open(name, 'r', encoding='utf-8') as f:
#         for line in f:
#             new_line = line.split(',')
#             my_dict[new_line[0].capitalize()] = float(new_line[1])
#         # print(my_dict)
#     with open('file_json.txt', 'w', encoding='utf-8') as f:
#         json.dump(my_dict, f, ensure_ascii=False, indent=2)
#
#
# convert('new_file.txt')


import json
__all__ = ['convert']



def convert(file_name: str) -> None:
    dic = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            li = line.split(',')

            dic[li[0].capitalize()] = float(li[1])
        # print(dic)
    with open('file_json.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)  # indent=2 перенос на новую строку


convert('new_file.txt')
