# Формат JSON

# Преобразование JSON в Python из файла

# import json
#
#
# with open('user.json', 'r', encoding='utf-8') as f:
#     json_file = json.load(f)
# print(f'{type(json_file) = }\n{json_file = }')
# print(f'{json_file["name"] = }')
# print(f'{json_file["address"]["geo"] = }')
# print(f'{json_file["email"] = }')

# Преобразование из строки

# import json
#
# json_text = """
# [
#     {
#         "userId": 1,
#         6
#         "id": 9,
#         "title": "nesciunt iure omnis dolorem tempora et
#         accusantium",
#         "body": "consectetur animi nesciunt iure dolore"
#     },
#     {
#         "userId": 1,
#         "id": 10,
#         "title": "optio molestias id quia eum",
#         "body": "quo et expedita modi cum officia vel magni"
#     },
#     {
#         "userId": 2,
#         "id": 11,
#         "title": "et ea vero quia laudantium autem",
#         "body": "delectus reiciendis molestiae occaecati non minima
#         eveniet qui voluptatibus"
#     },
#     {
#         "userId": 2,
#         "id": 12,
#         "title": "in quibusdam tempore odit est dolorem",
#         "body": "praesentium quia et ea odit et ea voluptas et"
#     }
# ]"""
# print(f'{type(json_text) = }\n{json_text = }')
# json_list = json.loads(json_text)
# print(f'{type(json_list) = }\t{len(json_list) = }\n{json_list = }')


# Преобразование Python в JSON в файл

#
# import json
#
#
# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#     "hobbies": ["кузнечное дело", "программирование",
#     "путешествия"],
#     "age": 35,
#     "children": [
#         {
#         "first_name": "Алиса",
#         "age": 5
#         },
#         {
#         "first_name": "Маруся",
#         "age": 3
#         }
#     ]
# }
# print(f'{type(my_dict) = }\n{my_dict = }')
# with open('new_user.json', 'w', encoding='utf-8') as f:
#     json.dump(my_dict, f, ensure_ascii=False)


# # Преобразование Python в JSON в строку
# import json
#
#
# my_dict = {
#     "first_name": "Джон",
#     "last_name": "Смит",
#     "hobbies": ["кузнечное дело", "программирование",
#     "путешествия"],
#     "age": 35,
#     "children": [
#         {
#             "first_name": "Алиса",
#             "age": 5
#         },
#         {
#             "first_name": "Маруся",
#             "age": 3
#         }
#     ]
# }
# dict_to_json_text = json.dumps(my_dict)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')
#
# dict_to_json_text = json.dumps(my_dict, ensure_ascii=False)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')


# Дополнительные параметры dump и dumps
import json

my_dict = {
    "id": 123,
    "name": "Clementine Bauche",
    "username": "Cleba",
    "email": "cleba@corp.mail.ru",
    "address": {
        "street": "Central",
        "city": "Metropolis",
        "zipcode": "123456"
    },
    "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'),
                 sort_keys=True)
print(res)
