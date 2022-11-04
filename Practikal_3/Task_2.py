import os
import random


# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def clear(): return os.system("cls")
clear()
n = int(input("Введите длину списка: "))
arr_min = int(input("Введите диапазон чисел списка(от): "))
arr_max = int(input("Введите диапазон чисел списка(до): "))
arr_1 = [random.randint(arr_min, arr_max) for i in range(n)]
arr_2 = list()
score = -1
for i in range(len(arr_1)//2 + 1 if len(arr_1) % 2 != 0 else len(arr_1)//2):
    arr_2.append(arr_1[i]*arr_1[score])
    score -= 1
print(f"{arr_1} => {arr_2}")
