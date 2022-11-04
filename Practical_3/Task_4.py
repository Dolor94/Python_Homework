import os


# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def clear(): return os.system("cls")
clear()
number = int(input("Введите число: "))
result = ""
while number != 0:
    result = str(number % 2) + result
    number //= 2
print(f"{number} => {result}")