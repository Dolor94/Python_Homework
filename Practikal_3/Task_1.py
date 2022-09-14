# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
import random

n = int(input("Введите длину списка: "))
list = [random.randint(0, 21) for i in range(n)]
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f"{list} -> сумма элементов на нечётных позициях = {sum}")
