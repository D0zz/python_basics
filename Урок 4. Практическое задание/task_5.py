"""
5. Реализовать формирование списка, используя функцию range()
и возможности генераторного выражения.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать лямбда-функцию и функцию reduce().
"""
from functools import reduce


def my_func(a, b):
    return a * b


my_list = [el for el in range(100, 1001, 2)]
print(my_list)
print(reduce(my_func, my_list))
