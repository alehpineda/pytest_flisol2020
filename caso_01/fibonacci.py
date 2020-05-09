def fib(n):
    if n < 0:
        raise ValueError('Error. Ingresa un numero positivo.')
    elif n in (0, 1):
        return n
    else:
        return fib(n - 1) + fib(n - 2)
