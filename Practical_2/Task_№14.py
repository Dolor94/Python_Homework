import os


# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def clear(): return os.system("cls")
clear()
number_N = int(input('Введите число N: '))
flag = True
x = 1
while flag:
    if x <= number_N:
        print(x, end=' ')
        x *= 2
        if x > number_N:
            flag = False
    else:
        flag = False
