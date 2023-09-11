def my_funktion(n):
    for i in range(2, n+1):
        flag = 0
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag += 1
                break
        if not flag:
            yield i

n = my_funktion(100)
print(*n)