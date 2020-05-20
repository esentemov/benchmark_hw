def func_recurs(b, n, my_list=[]):
    if n == 6:
        return 1

    my_list.append(b ** n)
    return b * func_recurs(b, n + 1, my_list)


# a = int(input("Введите число: "))
spisok = []
func_recurs(2, 2, spisok)
print((spisok))