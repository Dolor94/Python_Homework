import math
import os

def clear(): return os.system("cls")

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

clear()
print("Введите координаты точки 'А' в 2D пространстве:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("Введите координаты точки 'Б' в 2D пространстве:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
clear()
length = round(math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)), 2)
print(f"Расстояние между точками 'А' и 'Б' равняется: {length}")
