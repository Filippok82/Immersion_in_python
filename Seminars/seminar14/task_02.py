"""Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""


import re


def clean_text(text: str) -> str:
    """
            >>> clean_text("hello world")
            'hello world'
            >>> clean_text("HeLLo World")
            'hello world'
            >>> clean_text("HeLLo! World!")
            'hello world'
            >>> clean_text("HeLLo World во")
            'hello world '
            >>> clean_text("HeLLo World вол_шебСт0_12")
            'hello world '
            """


    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()



if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
