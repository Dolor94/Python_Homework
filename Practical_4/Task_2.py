# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
i = 2 
arr = []
user_number = number
while i <= number:
    if number % i == 0:
        arr.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {user_number} приведены в списке: {arr}")