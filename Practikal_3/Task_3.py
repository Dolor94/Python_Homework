import os
import random


# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def clear(): return os.system("cls")
clear()
n = int(input("Введите длину списка: "))
arr_min = float(input("Введите диапазон чисел списка(от): "))
arr_max = float(input("Введите диапазон чисел списка(до): "))
arr = [random.uniform(arr_min, arr_max) for i in range(n)]
arr_1 = list()
arr_2 = list()
for i in arr:
    arr_1.append(f'{i:.2f}')
for i in range(len(arr)):
    arr_2.append(int(arr[i]*100 % 100))
print(f"{arr_1} => {(max(arr_2) - min(arr_2))/100}")
