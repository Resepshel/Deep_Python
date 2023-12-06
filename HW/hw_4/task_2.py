# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def change_dict(*, key, values):
    new_dict = {}
    for el in range(len(key)):
        try:
            hash(values[el])
            new_dict[values[el]] = key[el]
        except:
            new_dict[str(values[el])] = key[el]
    return new_dict


dict_data = {'1': 42,
             '2': 'strochka',
             '3': [123, 111],
             '4': (123, 111),
             '5': {123, 111}}

result_dict = change_dict(key=list(dict_data.keys()), values=list(dict_data.values()))
print(result_dict.keys(), result_dict.values())
