# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

HEX_NUM = 16
ONE = 1

number = int(input('Введите целое число: '))
result = ''
print(f'Проверка {hex(number)}')

while number != 0:
    mod = number % HEX_NUM
    if mod == 10:
        result = 'A' + result
    elif mod == 11:
        result = 'B' + result
    elif mod == 12:
        result = 'C' + result
    elif mod == 13:
        result = 'D' + result
    elif mod == 14:
        result = 'E' + result
    elif mod == 15:
        result = 'F' + result
    else:
        result = str(mod) + result
    number //= HEX_NUM
print(result)

