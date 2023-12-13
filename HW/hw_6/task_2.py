# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
import random as r


def generate_random_queen_placement():
    # Генерируем случайные координаты для 8 ферзей
    queens = [(r.randint(1, 8), r.randint(1, 8)) for _ in range(8)]
    return queens


def check_positions(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1]:
                return False

    for i in range(8):
        for j in range(i + 1, 8):
            if abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False

    return True


if __name__ == '__main__':
    positions = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 3), (6, 1), (7, 7), (8, 5)]
    result = check_positions(positions)
    print(result)
    random_queen_placement = generate_random_queen_placement()
    print(check_positions(random_queen_placement))
