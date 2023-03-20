# ФАЙЛЫ
# Метод open()

# f = open('text_data.txt', encoding='utf-8')
# print(f)
# print(list(f))

"""● Режимы работы с файлами
Рассмотрим доступные режимы работы с файлами.
➢ 'r' — открыть для чтения (по умолчанию)
➢ 'w' — открыть для записи, предварительно очистив файл
➢ 'x' — открыть для эксклюзивного создания. Вернёт ошибку, если файл уже
существует
➢ 'a' — открыть для записи в конец файла, если он существует
➢ 'b' — двоичный режим
➢ 't' — текстовый режим (по умолчанию)
➢ '+' — открыты для обновления (чтение и запись)"""

# Метод close()

# f = open('text_data.txt', 'a', encoding='utf-8')
# f.write('Окончание файла\n')
# f.close()

# Прочие необязательные параметры функции open

# f = open('bin_data', 'wb', buffering=64)
# f.write(b'X' * 1200)
# f.close()
#

# _______________________________________________________________

# f = open('data.txt', 'wb')
# f.write('Привет, '.encode('utf-8') + 'мир!'.encode('cp1251'))
# f.close()
#
# # f = open('data.txt', 'r', encoding='utf-8')
# # print(list(f)) # UnicodeDecodeError: 'utf-8' codec can't decode byte 0xec in position 14: invalid continuation byte
# # f.close()
#
# f = open('data.txt', 'r', encoding='utf-8', errors='replace')
# print(list(f))
# f.close()


# Менеджер контекста with open

# with open('text_data.txt', 'r+', encoding='utf-8') as f:
#     print(list(f))
# print(f.write('Пока')) # ValueError: I/O operation on closed file.


# ________________________________________________________________________

# with open('text_data.txt', 'r+', encoding='utf-8') as f1, \
#         open('bin_data', 'rb') as f2, \
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))

# для более новой версии python

# with (
#         open('text_data.txt', 'r+', encoding='utf-8') as f1,
#         open('bin_data', 'rb') as f2,
#         open('data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
# ):
#     print(list(f1))
#     print(list(f2))
#     print(list(f3))
f = open('bin_data', 'wb', buffering=64)
f.write(b'X' * 1200)
f.close()
