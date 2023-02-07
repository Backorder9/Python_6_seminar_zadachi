'''
Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
'''
import random

def list_generation():
    n = int(input('Введите количество элементов списка: '))
    min1 = int(input('Введите нижнюю границу диапазона значений элементов списка: '))
    max2 = int(input('Введите верхнюю границу диапазона значений элементов списка: '))
    return [random.randint(min(min1, max2), max(min1, max2)) for i in range(n)]

numbers_list = list_generation()
result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')