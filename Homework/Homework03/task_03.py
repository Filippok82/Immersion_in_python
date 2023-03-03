# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.
#

import operator

text = 'Метод split разделяет строку по разделителю, разбиение происходить слева направо. ' \
       'Возвращает список (list) состоящий из кусков строки. Метод split имеет два именованных аргумента: ' \
       'sep - разделитель, любой символ буква или цифра по которой делится строка. По умолчанию sep= None' \
       ' и разделителем будет пробел, но все пробелы спереди и сзади строки, а также пустые строки удаляются.' \
       'мaxsplite-максимальное количество (то есть не более чем мaxsplite раз, меньше можно) раз на которое будет' \
       ' разбита строка. По умолчанию maxsplite=-1. «-1» обозначает не ограниченное количество разбиений. ' \
       'Если мaxsplite меньше количества разделителей в строке, то из оставшегося куска строки получается' \
       ' один элемент списка.'

text1 = text.replace('.', '').replace('-', '').replace(':', '').replace(',', '').replace('(', '').replace(')',
                                                                                                          '').lower()
print(text1)
text2 = text1.split()
print(len(text2))
text3 = []
for item in text2:
    if text2.count(item) > 1:
        text3.append(item)
print(text3)

dict1 = {}
for item in text3:
    dict1[item] = text3.count(item)

print(dict1)

sort_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
res_dict = dict(sort_dict.items())
print(res_dict)
res_list = list(res_dict)
print(len(res_list))
print(res_list[5:15])
