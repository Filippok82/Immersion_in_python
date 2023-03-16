# Методы перемещения в файле
# Метод tell

# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'w', encoding='utf-8') as f:
#     print(f.tell())
#     for line in text:
#         f.write(f'{line}\n')
#         print(f.tell())
#     print(f.tell())
# print(f.tell()) # ValueError: I/O operation on closed file.

# Метод seek

# last = before = 0
# text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
#         'Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
#         'Accusantium alias amet fugit iste neque non odit quiasaepe totam velit?', ]
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#         print(f'{last = }, {before = }')
#     print(f'{last = }, {before = }')
#     print(f'{f.seek(before, 0) = }')
#     f.write('\n'.join(text))

# Метод truncate

# last = before = 0
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     while line := f.readline():
#         last, before = f.tell(), last
#     print(f.seek(before, 0))
#     print(f.truncate())

#__________________________________________________________

# size = 64
# with open('new_data.txt', 'r+', encoding='utf-8') as f:
#     print(f.truncate(size))


