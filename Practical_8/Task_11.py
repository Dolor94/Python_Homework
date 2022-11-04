# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части
import random

n = int(input("Введите длину списка: "))
arr = [random.uniform(1.00, 21.00) for i in range(n)]
arr_1 = list()
arr_2 = list()
for i in arr:
    arr_1.append(f'{i:.2f}')
for i in range(len(arr)):
    arr_2.append(int(arr[i]*100 % 100))
print(f"{arr_1} => {(max(arr_2) - min(arr_2))/100}")
