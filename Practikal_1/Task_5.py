import os

def clear(): return os.system("cls")

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).

clear()
x = int(input('input x: '))
y = int(input('input y: '))
if x > 0 and y > 0:
    print('1')
if x < 0 and y > 0:
    print('2')
if x < 0 and y < 0:
    print('3')
if x > 0 and y < 0:
    print('4')
