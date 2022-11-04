import os


# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# Упрощенный вариант
# user_number = input('Введите число: ')
# sum_numbers = 0
# for i in user_number:
#     if i.isdigit():
#         sum_numbers += int(i)
# print(f"{user_number} -> {sum_numbers}")

def clear(): return os.system("cls")
clear()
user_number = input("Введите число: ")
check_number = user_number
sum_numbers = 0
while check_number > 0:
    sum_numbers += check_number%10
    check_number //= 10
print(f"{user_number} -> {sum_numbers}")
