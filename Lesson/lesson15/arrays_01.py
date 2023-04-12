"""Модуль array"""

# from array import array, typecodes
#
# byte_array = array('B', (1, 2, 3, 255))
# print(byte_array)
# print(typecodes)

"""Массивы поддерживают методы списка list, поэтому использование их интуитивно
понятно. """

# from array import array
#
# long_array = array('l', [-6000, 800, 100500])
# long_array.append(42)
# print(long_array)
# print(long_array[2])
# print(long_array.pop())


"""При этом массив не позволит добавить значение, если оно выходит за пределы
диапазона, заданного кодом типа при создании. Так же будет поднята ошибка при
несоответствии типа"""

from array import array
long_array = array('l', [-6000, 800, 100500])
# long_array.append(2**32) # OverflowError: Python int too large to convert to C long
# long_array.append(3.14) # TypeError: 'float' object cannot be interpreted as an integer
