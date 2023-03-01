# Список
#
# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]

# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list[0])
# print(my_list[5])
# print(my_list[-1])

#Метод append

# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)

#Метод extend

# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# #my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list)

#Метод pop

# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# #err = my_list.pop(10) # IndexError: pop index out of range

#Метод count

# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2)
# print(spam)
# eggs = my_list.count(3)
# print(eggs)

# Метод index
#
# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4)
# print(spam)
# eggs = my_list.index(4, spam + 1, 90)
# print(eggs)
# #err = my_list.index(3) # ValueError: 3 is not in list

#Метод insert
#
# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555)
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
# print(my_list)

#Метод remove

my_list = [2, 4, 6, 8, 10, 12, 6]
my_list.remove(6)
print(my_list)
my_list.remove(3) # ValueError: list.remove(x): x not in list
print(my_list)