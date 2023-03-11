# import

# import sys
#
#
# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep='\n')

#Использование from и as

# from sys import builtin_module_names, path
#
#
# print(builtin_module_names)
# print(*path, sep='\n')

#__________________________________________________________

# import random as rnd
# from sys import builtin_module_names as bmn, path as p
#
#
# print(bmn)
# print(*p, sep='\n')
# print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined


# Плохой import * (импорт со звездочкой)

from random import randint

__all__ = ['func', '_secret']

SIZE = 100
_secret = 'qwerty'
__top_secret = '1q2w3e4r5t6y'

def func(a: int, b: int) -> str:
    z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
    return z
result = func(1, 6)
