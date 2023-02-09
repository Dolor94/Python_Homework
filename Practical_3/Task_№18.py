import random
import os


# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

def clear(): return os.system("cls")
clear()
len_arr = int(input("Введите длину массива: "))
list = [random.randint(0, 21) for i in range(len_arr)]
number = int(input('Введите число: '))
print()
print(*list)
print()
find_number = list[0]
for i in list:
    if abs(i - number) < abs(find_number - number):
        find_number = i
print(f'К числу {number} ближайшим по величине элемент является {find_number}')
