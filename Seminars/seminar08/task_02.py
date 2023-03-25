"""Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться."""
import json

__all__ = ['name_id_access_level']


def name_id_access_level(name_file) -> None:
    my_dict = {}
    with open(name_file, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            my_dict = data
            print(type(my_dict))
            print(my_dict)
        except json.decoder.JSONDecodeError:
            print("")

    while True:
        user_name = input('Имя:')
        if user_name == '':
            break
        id_user = input('Идентификатор:')
        level = input('Уровень доступа:')
        my_dict01 = {id_user: user_name}
        if my_dict.get(level) is None:
            my_dict[level] = my_dict01
        else:
            k = my_dict.get(level)
            k.update(my_dict01)
    with open(name_file, 'w', encoding='utf-8') as f:
        json.dump(my_dict, f, ensure_ascii=False, indent=2)


name_id_access_level("ident.json")





