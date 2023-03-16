# Чтение файла: целиком, через генератор
# Чтение в список

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     print(list(f))

# Чтение методом read

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     res = f.read()
#     print(f'Читаем первый раз\n{res}')
#     res = f.read()
#     print(f'Читаем второй раз\n{res}')

#________________________________________________________________________

# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.read(SIZE):
#         print(res)

# Чтение методом readline

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline():
#         print(res)

#_____________________________________________________________________________

# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     while res := f.readline(SIZE):
#         print(res)


# Чтение циклом for

# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line, end='')


#_____________________________________________________________________________

# SIZE = 100
# with open('text_data.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line[:-1])
#         print(line.replace('\n', ''))
