import os

def clear(): return os.system("cls")

# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

clear()
n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Ошибка, повторите ввод')
elif n == 1:
    print('x > 0 и y > 0')
elif n == 2:
    print('x < 0 и y > 0')
elif n == 3:
    print('x < 0 и y < 0')
elif n == 4:
    print('x > 0 и y < 0')