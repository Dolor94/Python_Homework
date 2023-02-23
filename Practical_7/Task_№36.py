import os


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

def clear(): return os.system("cls")
clear()
def operation_table(func, row=6, colums=6):
    for i in range(row):
        for j in range(colums):
            print(f'{func(i+1, j+1)}', end=' \t')
        print()

operation_table(lambda x, y: x * y, 6)
