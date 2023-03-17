# Файловая система
#
#Текущий каталог

# import os
# from pathlib import Path
#
#
# print(os.getcwd())
# print(Path.cwd())

#______________________________________________

# import os
# from pathlib import Path
#
#
# print(os.getcwd())
# print(Path.cwd())
# os.chdir('../..')
# print(os.getcwd())
# print(Path.cwd())

# Создание каталогов

# import os
# from pathlib import Path
#
#
# os.mkdir('new_os_dir')
# Path('new_path_dir').mkdir()

#____________________________________________________

# import os
# from pathlib import Path
#
#
# # os.makedirs('dir/other_dir/new_os_dir')
# # Path('some_dir/dir/new_path_dir').mkdir() # FileNotFoundError
# Path('some_dir/dir/new_path_dir').mkdir(parents=True)


# ● Удаление каталогов

# import os
# from pathlib import Path
#
#
# # os.rmdir('dir') # OSError
# # Path('some_dir').rmdir() # OSError
# os.rmdir('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').rmdir()
#_________________________________________________________

# import shutil
#
# shutil.rmtree('dir/other_dir')
# shutil.rmtree('some_dir')

#  Формирование пути

# import os
# from pathlib import Path
#
#
# file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
# print(f'{file_1 = }\n{file_1}')
#
# file_2 = Path().cwd() / 'dir' / 'new_file.txt'
# print(f'{file_2 = }\n{file_2}')


# Чтение данных о каталогах


# import os
# from pathlib import Path
#
# print(os.listdir())
#
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(obj)

#● Проверка на директорию, файл и ссылку


# import os
# from pathlib import Path
#
#
# dir_list = os.listdir()
# for obj in dir_list:
#     print(f'{os.path.isdir(obj) = }', end='\t')
#     print(f'{os.path.isfile(obj) = }', end='\t')
#     print(f'{os.path.islink(obj) = }', end='\t')
#     print(f'{obj = }')
#
# p = Path(Path().cwd())
# for obj in p.iterdir():
#     print(f'{obj.is_dir() = }', end='\t')
#     print(f'{obj.is_file() = }', end='\t')
#     print(f'{obj.is_symlink() = }', end='\t')
#     print(f'{obj = }')

# Обход папок через os.walk()

# import os
# for dir_path, dir_name, file_name in os.walk(os.getcwd()):
#     print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')

# Работа с файлами

# Переименование файлов

# import os
# from pathlib import Path
#
#
# os.rename('old_name.py', 'new_name.py')
#
# p = Path('old_file.py')
# p.rename('new_file.py')
#
# Path('new_file.py').rename('newest_file.py')

#Перемещение файлов

# import os
# from pathlib import Path
#
#
# os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_name.py'))
# old_file = Path('new_name.py')
# new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)

# Копирование файлов

# import shutil
#
#
# shutil.copy('one.txt', 'dir')
# shutil.copy2('two.txt', 'dir')

#_______________________________________________

# import shutil
#
# shutil.copytree('dir', 'one_more_dir')

# ● Удаление файлов

# import shutil
#
# shutil.rmtree('dir')


# Если же необходимо удалить один файл, можно воспользоваться следующими
# вариантами:

import os
from pathlib import Path


os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()