import os


# Задача 2: - (HARD) Найдите сумму цифр любого вещественного или целого числа. 
# Можно использовать decimal. Через строку решать нельзя.

def clear(): return os.system("cls")
clear()
user_number = input('Введите число: ')
sum_numbers = 0
for i in user_number:
    if i.isdigit():
        sum_numbers += int(i)
print(f"Сумма цифр числа {user_number} = {sum_numbers}")
