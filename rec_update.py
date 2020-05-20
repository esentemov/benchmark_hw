def func_recurs(n):
    a = 2
    if n == 0:
        return 1
    r = func_recurs(n - 1)
    return a * r

# print(func_recurs(5))