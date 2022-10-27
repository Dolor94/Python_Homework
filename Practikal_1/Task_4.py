import os


# задача 4 HARD необязательная Напишите простой калькулятор, 
# который считывает с пользовательского ввода три строки: первое число, второе число и операцию, 
# после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# ивыводит результат на экран.
# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.
# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
# Обратите внимание, что на вход программе приходят вещественные числа.

def clear(): return os.system("cls")
clear()
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
def summ(a, b):
    return print(f"{a} + {b} = {a+b}")

def sub(a, b):
    return print(f"{a} - {b} = {a-b}")

def mul(a, b):
    return print(f"{a} * {b} = {a*b}")

def div_1(a, b):
    return print(f"{a} / {b} = {a/b}")

def pow(a, b):
    return print(f"{a} * {b} = {a*b}")

def mod(a, b):
    return print(f"{a} % {b} = {a%b}")

def div_2(a, b):
    return print(f"{a} // {b} = {a//b}")

operator = input("Какую операцию желаете выполнить (+, -, /, , *, %, //): ")

if operator == "+":
    summ(a,b)
elif operator == "-":
    sub(a,b)
elif operator == "/" or operator == "//":
    if operator == "/" or operator == "//" and b == 0:
        print("Деление на 0!")
    elif operator == "/":
        div_1(a,b)
    elif operator == "//":
        div_2(a,b)
elif operator == "*":
    mul(a,b)
elif operator == "**":
    pow(a,b)
elif operator == "%":
    mod(a,b)
else: 
    print("Такого оператора нет!")