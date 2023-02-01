import os


# Задача 2: Найдите сумму цифр трехзначного числа.

def clear(): return os.system("cls")
clear()
number = int(input('Введите трехзначное число: '))
sum_numbers = 0
flag = True
if number < 100 or number > 999:
    while flag:
        if number < 100 or number > 999:
            number = int(input('Ошибка! Введите трехзначное число: '))
        else:
            flag = False

number1 = number
while number1 != 0:
    sum_numbers += number1 % 10
    number1 //= 10

print(f'Сумма цифр числа {number} = {sum_numbers}')
