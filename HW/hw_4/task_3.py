# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

# Задание №6 Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
import decimal as d

# Константы
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = d.Decimal(5_000_000)
RICHNESS_TAX = d.Decimal(10) / d.Decimal(100)
WITHDRAW_PERCENT = d.Decimal(15) / d.Decimal(1000)
ADD_PERCENT = d.Decimal(3) / d.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = d.Decimal(0)
count = 0

# Списки для операций поступления и снятия средств
deposit_history = []
withdraw_history = []

# Функция для вывода баланса и завершения программы
def exit_program(balance):
    print(f'Возьмите карту, на которой {balance} у.е.')

# Функция для внесения депозита
def deposit(account):
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    account += amount
    deposit_history.append(amount)
    return account, amount

# Функция для снятия средств
def withdraw(account):
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (
        MIN_REMOVAL if withdraw_tax < MIN_REMOVAL else
        MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax
    )
    if account >= amount + withdraw_tax:
        account -= (amount + withdraw_tax)
        withdraw_history.append((amount, withdraw_tax))
        return account, amount, withdraw_tax
    else:
        return account, None, withdraw_tax

# Функция для расчета налога на богатство
def calculate_richness_tax(account):
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        return account, percent
    return account, 0

# Функция для начисления бонуса
def calculate_bonus(account):
    bonus_percent = account * ADD_PERCENT
    account += bonus_percent
    return account, bonus_percent

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        exit_program(account)
        break
    if command == CMD_DEPOSIT:
        account, amount = deposit(account)
        count += 1
        print(f'Пополнение карты на {amount} у.е.\nИтого на карте {account} у.е.')
    elif command == CMD_WITHDRAW:
        account, amount, withdraw_tax = withdraw(account)
        if amount is not None:
            count += 1
            print(f'Снятие с карты {amount} у.е.\nКомиссия за снятие {withdraw_tax} у.е.\n'
                  f'На карте осталось {account} у.е.')
        else:
            print(f'Недостаточно денег для выполнения операции\n'
                  f'Затребованная сумма {amount} у.е., Комиссия составила {withdraw_tax} у.е.\n'
                  f'На карте {account} у.е.')
    account, richness_tax = calculate_richness_tax(account)
    if richness_tax > 0:
        print(f'Удержан налог на богатство {RICHNESS_TAX * 100}% в размере {richness_tax} у.е.\n'
              f'Итого на карте {account} у.е.')
    if count % COUNT_OPER == 0:
        account, bonus_percent = calculate_bonus(account)
        print(f'На счёт начислено {ADD_PERCENT * 100}%, составляющие {bonus_percent} у.е.\n'
              f'Итого на карте {account} у.е.')

print("История операций поступления:")
for i, amount in enumerate(deposit_history, 1):
    print(f"Операция {i}: Внесено {amount} у.е.")

print("История операций снятия:")
for i, (amount, withdraw_tax) in enumerate(withdraw_history, 1):
    print(f"Операция {i}: Снято {amount} у.е., Комиссия {withdraw_tax} у.е.")






