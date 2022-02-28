def fib(n):
    x, y = 1, 1
    for _ in range(n):
        yield x
        x, y = y, x + y
