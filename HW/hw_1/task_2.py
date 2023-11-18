# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

LOWER_LIMIT = 0
UPPER_LIMIT = 100000
ONE = 1
TWO = 2

counter = TWO
number = LOWER_LIMIT - ONE

while number < LOWER_LIMIT or number > UPPER_LIMIT:
    number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))

while counter**TWO <= number and number % counter != 0:
    counter += 1

if counter**TWO > number:
    res = f'Число {number} простое'
else:
    res = f'Число {number} составное'

print(res)
