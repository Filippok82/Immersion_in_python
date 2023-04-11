""" Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно."""



def my_func03(text: str = None) -> dict[str, int]:
    my_dict = {}
    while True:
        try:
            data = (input(text))
            num_01, num_02 = map(int, data.split())
            for i in range(min(num_01, num_02), max(num_01, num_02) + 1):
                my_dict[chr(i)] = i
            return my_dict

        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')




if __name__ == '__main__':
    my_str = 'Введите два числа через пробел: '
    print(my_func03(my_str))
