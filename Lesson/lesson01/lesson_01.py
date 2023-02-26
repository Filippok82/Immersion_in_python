# name = 'Alex'
# age = None
# a = 42
# print(id(a))
#
# a = 'hello'
# print(id(a))
#
# print(name, age, a, 524, 'cat', sep=' (=^.^=) ', end='#')
# print('dog')
#
# result = input(' Print your text')
# print('Ты написал ', result)

# ADULT = 18
# age = float(input('Ваш возраст: '))
# how_old = age - ADULT
# print(how_old, "лет назад ты стал совершеннолетним")
#

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')

data = 0
while data < 100:
    data += 3
    if data % 19 == 0:
        continue
    data += 1
    if data % 40 == 0:
        break
else:
    data += 5
print(data)
