import os

# задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def clear(): return os.system("cls")
clear()
first_arr = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {first_arr}")
new_arr = []
[new_arr.append(i) for i in first_arr if i not in new_arr]
print(f"Список из неповторяющихся элементов: {new_arr}")
