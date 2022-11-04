import os
import random


# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def clear(): return os.system("cls")
clear()
n = int(input("Введите длину списка: "))
list_min = int(input("Введите диапазон чисел списка(от): "))
list_max = int(input("Введите диапазон чисел списка(до): "))
list = [random.randint(list_min, list_max) for i in range(n)]
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f"{list} -> сумма элементов на нечётных позициях = {sum}")
