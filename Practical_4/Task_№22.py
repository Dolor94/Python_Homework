import os


# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

def clear(): return os.system("cls")
clear()
len_arr_1 = int(input('Введите длину 1-го списка: '))
len_arr_2 = int(input('Введите длину 2-го списка: '))

arr_1 = []
arr_2 = []

for i in range(0, len_arr_1):
    arr_1.append(int(input(f'Введите значение {i}-го элемента 1-го списка: ')))
    
print()

for i in range(0, len_arr_2):
    arr_2.append(int(input(f'Введите значение {i}-го элемента 2-го списка: ')))

arr_3 = []

i = 0
while i < len_arr_1:
    j = 0
    while j < len_arr_2:
        if arr_1[i] == arr_2[j]:
            arr_3.append(arr_1[i])
        j += 1
    i += 1
            
print(*arr_1)
print(*arr_2)
print(*sorted(set(arr_3)))
