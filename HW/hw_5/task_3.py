# Создайте функцию генератор чисел Фибоначчи

def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


point = 20
fib = fib_gen()
for _ in range(point):
    print(next(fib))

