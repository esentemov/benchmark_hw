from simple_benchmark import benchmark

from rec import func_recurs
from round import func_round
import matplotlib.pyplot as plt

func = [func_recurs, func_round]
arguments = {}
for i in range(20):
    arguments['i' + str(i)] = i
print(arguments)
arguments_name = 'natural numbers'

aliases = {func_round: "Циклическая функция", func_recurs: "Рекурсия"}
b = benchmark(func, arguments, arguments_name, function_aliases=aliases)
b.plot()
plt.show(b)
