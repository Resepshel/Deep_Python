# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# number = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ONE = 1
TEN = 10

secret_num = randint(LOWER_LIMIT, UPPER_LIMIT)
counter = ONE

while counter <= TEN:
    print(f'Попытка номер {counter}')
    num = LOWER_LIMIT - ONE
    while num < LOWER_LIMIT or num > UPPER_LIMIT:
        num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))

    if secret_num == num:
        print(f'Вы угадали! Это число {num}')
        break
    elif secret_num > num:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')

    counter += 1
else:
    print('Вы не угадали :(')


