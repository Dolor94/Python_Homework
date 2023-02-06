import os


# задача 4 НЕГА Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def clear(): return os.system("cls")
clear()
k = int(input('Введите число: '))
arr_numbers = []
a = 1
b = 1
for i in range(k):
    arr_numbers.append(a)
    a, b = b, a + b
a = 0
b = 1
for i in range(k+1):
    arr_numbers.insert(0, a)
    a, b = b, a - b

print(*arr_numbers)