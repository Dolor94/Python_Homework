import os


# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии

def clear(): return os.system("cls")
clear()
number_A = int(input('Введите число: '))
number_B = int(input('Введите степень: '))

def search_number(number_A, number_B):
    if number_B <= 1:
        return number_A
    if number_B != 1:
        return(number_A * search_number(number_A, number_B-1))

x = search_number(number_A, number_B) 
print(f'Число {number_A} в степени {number_B} = {x}')