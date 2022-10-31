import os


# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой. Нельзя юзать find или count.

def clear(): return os.system("cls")
clear()
flag = True
while flag:
    user_text_1 = input("Введите строку: ")
    if user_text_1 == "":
        print("Ошибка! Введите освновную строку!")
    else:
        flag = False
flag = True
while flag:
    user_text_2 = input("Введите подстроку: ")
    if user_text_2 == "":
        print("Ошибка! Введите искомую подстроку!")
    else:
        flag = False
check = 0
i = 0
while i < len(user_text_1.split()):
    if user_text_2 == user_text_1.split()[i]:
        check += 1
    i += 1
print(f"Основная строка: {user_text_1}")
print(f"Подстрока: {user_text_2}")
print(f"Количество вхождений подстроки в основную строку = {check}")