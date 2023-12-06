# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
ONE = 1
result = []

for item in set(data):
    if data.count(item) > ONE:
        result.append(item)

print(result)
