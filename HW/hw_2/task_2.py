# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions

import fractions
import math

fisrt_frac = input('Введите первую дробь вида "a/b": ')
second_frac = input('Введите вторую дробь вида "a/b": ')

a1, b1 = fisrt_frac.split('/')
a2, b2 = second_frac.split('/')

a_mult = int(a1) * int(a2)
b_mult = int(b1) * int(b2)
a_sum = int(a1) * int(b2) + int(a2) * int(b1)
b_sum = int(b1) * int(b2)
gcd_mult = math.gcd(a_mult, b_mult)
gcd_sum = math.gcd(a_sum, b_sum)

if gcd_mult:
    a_mult //= gcd_mult
    b_mult //= gcd_mult
if gcd_sum:
    a_sum //= gcd_sum
    b_sum //= gcd_sum

mult_frac = f'{a_mult}/{b_mult}'
sum_frac = f'{a_sum}/{b_sum}'

print(f'Сумма: {sum_frac}')
print(f'Произведение: {mult_frac}')

test_1 = fractions.Fraction(int(a1), int(b1))
test_2 = fractions.Fraction(int(a2), int(b2))
print(f'Проверка\nСумма: {test_1 + test_2}, произведение: {test_1 * test_2}')
