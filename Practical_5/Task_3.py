import os


# задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def clear(): return os.system("cls")
clear()

def del_txt(x):
    return False if 'абв' in x else True
    # for i in range(len(x)-2):
    #     if (x[i]+x[i+1]+x[i+2]) == 'абв':
    #         k = False
    # return k

user_txt = input('Введите текст: ')
user_txt = user_txt.split()
print("вводные данные")
print(*user_txt)
user_txt = list(filter(del_txt, user_txt))
print("выходные данные")
print(*user_txt)
