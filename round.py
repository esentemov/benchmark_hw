def func_round(b, n):
    my_list = []
    for i in range(2, n+1):

        my_list.append(b**i)
    return my_list



# a = int(input("Введите число: "))
print(func_round(2, 5))
