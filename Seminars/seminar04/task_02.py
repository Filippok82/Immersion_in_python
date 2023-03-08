# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def my_func02(text: str) -> list[int]:
    my_list = set()
    for item in text:
        my_list.add(ord(item))
    my_list = sorted(my_list, reverse=True)
    return my_list


my_str = input('Введите строку:')
print(my_func02(my_str))
