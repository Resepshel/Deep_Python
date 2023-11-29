# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.

WEIGHT_CAPACITY = 25

things = {'Палатка': 15,
          'Спальник': 5,
          'Еда': 10,
          'Аптечка': 3,
          'Вода': 7,}

items = list(things.keys())

current_weight = 0
current_things = []
combination = set()

for k, v in things.items():
    current_weight += v
    if current_weight <= WEIGHT_CAPACITY:
        current_things.append(k)
    else:
        current_weight -= v
print(current_things)
