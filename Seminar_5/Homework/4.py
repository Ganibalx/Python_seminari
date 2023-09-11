def fib():
    flag = 0
    while True:
        f = (1+5**0.5)/2
        rez = (f**flag-(-f)**(-flag))/(2*f-1)
        yield int(rez)
        flag += 1


x = fib()
print([next(x) for i in range(11)])
