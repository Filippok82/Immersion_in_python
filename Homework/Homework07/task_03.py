from PythonGB.Homework.Homework07.task01.task_02 import desired_name, file_extension
from PythonGB.Seminars.seminar07 import task_01, task_02
from PythonGB.Seminars.seminar07 import task_03
from PythonGB.Seminars.seminar07 import task_04
from PythonGB.Seminars.seminar07.task_04 import expansion, count_file



sem07_01 = task_01.func01(5, "text_file.txt")
sem07_02 = task_02.func02(5, "data.txt")
sem07_03 = task_03.open_files('text_file.txt', 'data.txt')
sem07_04 = task_04.gen_file(expansion, count_file)

hw = task_02.group_renaming(count_file,desired_name, file_extension )



