# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

number = int(input("Введите число: "))

result = ""
while number != 0:
    result = str(number % 2) + result
    number //= 2
print(f"{number} => {result}")