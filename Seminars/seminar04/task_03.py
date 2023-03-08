#  Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.

def my_func03(a: str) -> dict[str, int]:

    my_dict = {}
    num_01, num_02 = map(int, a.split())
    for i  in range(min(num_01,num_02), max(num_01,num_02)+1):
        my_dict[chr(i)]=i
    return my_dict


my_str = input('Введите строку:')
print(my_func03(my_str))
