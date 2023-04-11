"""Создайте функцию, которая удаляет из текста все символы
кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.
"""

# import re
# def clean_text(text: str) -> str:
#     cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
#     return cleaned_text.lower()
#
#
# user_text = "Every утро i go на work! 12334_12"
# print(clean_text(user_text))

from string import ascii_letters


def delfromtext(text: str):
    a = ''
    for char in text:
        if char in ascii_letters or char == ' ':
            a += char
    return a.lower()


print(delfromtext('роме букв латинского. алфавита 123/ апраоп! hjjkg'))