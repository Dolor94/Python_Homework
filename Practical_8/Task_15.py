# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

first_arr = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {first_arr}")
new_arr = []
[new_arr.append(i) for i in first_arr if i not in new_arr]
print(f"Список из неповторяющихся элементов: {new_arr}")