# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random

n = int(input("Введите длину списка: "))
arr_1 = [random.randint(1, 21) for i in range(n)]
arr_2 = list()
score = -1
for i in range(len(arr_1)//2 + 1 if len(arr_1) % 2 != 0 else len(arr_1)//2):
    arr_2.append(arr_1[i]*arr_1[score])
    score -= 1
print(f"{arr_1} => {arr_2}")
