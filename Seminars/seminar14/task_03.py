"""Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)"""

import unittest
import re


def clean_text(text: str) -> str:
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned_text.lower()


# print(clean_text('hello world'))


class TestCaseName(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(clean_text("hello world"), 'hello world')

    def test_registr(self):
        self.assertEqual(clean_text("HellO woRld"), 'hello world')

    def test_no_punctuation(self):
        self.assertEqual(clean_text("hello, world..."), 'hello world')

    def test_language(self):
        self.assertEqual(clean_text("hello world ворлд"), 'hello world ')

    def test_all(self):
        self.assertEqual(clean_text("HellO !woRld, ворлд"), 'hello world ')


if __name__ == '__main__':
    unittest.main(verbosity=2)