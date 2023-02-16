import os


# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def clear(): return os.system("cls")
clear()
number_A = int(input('Введите 1-е число: '))
number_B = int(input('Введите 2-е число: '))

def sum(number_A, number_B):
    if number_A == 0:
        return number_B
    else:
        return sum(number_A-1, number_B+1)

x = sum(number_A, number_B)    
print(f'Cумма чисел {number_A} и {number_B} = {x}')