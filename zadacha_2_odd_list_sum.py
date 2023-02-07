'''
Найти сумму чисел списка стоящих на нечетной позиции.
'''

import random

def list_generation():
    n = int(input('Введите количество элементов списка: '))
    min1 = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    max2 = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
    return [random.randint(min(min1, max2), max(min1, max2)) for i in range(n)]

numbers_list = list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')