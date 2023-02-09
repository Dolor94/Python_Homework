import random
import os


# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai . Последняя строка содержит число X

def clear(): return os.system("cls")
clear()
len_arr = int(input("Введите длину массива: "))
list = [random.randint(0, 21) for i in range(len_arr)]
find_number = int(input('Введите число которое нужно найти в массиве: '))
print()
print(*list)
print()
print(f'Ищем число {find_number} в заданном массиве')
x = 0
for i in range(len(list)):
    if find_number == list[i]:
        x += 1
print(f'В заданном массиве число {find_number} встречается {x} раз')
