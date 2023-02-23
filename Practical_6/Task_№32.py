import os
from random import randint


# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def clear(): return os.system("cls")
clear()
len_array = int(input('Введите общее количество элементов массива: '))
min_num_array = int(input('Введите минимальное значение массива: '))
max_num_array = int(input('Введите максимальное значение массива: '))
min_num = int(input('Введите минимальное значение диапазона: '))
max_num = int(input('Введите максимальное значение диапазона: '))

array = []
print()
for i in range(len_array):
    array.append(randint(min_num_array, max_num_array))
print('Задан массив: ','\n',*array)

print('Индексы элементов заданного диапазона: ')
for i in range(len(array)):
    if min_num <= array[i] <= max_num:
        print(i, end=' ')
