import os


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

def clear(): return os.system("cls")
clear()
Petya = 0  # Можно сделать ввод данных через int(input())
Seryozha = None
Katya = None
flag = True
while flag:
    Seryozha = Petya
    Katya = (Petya+Seryozha)*2
    if Katya / 2 == 0:
        Petya += 1
    elif Petya + Seryozha == Katya / 2:
        flag = False
        
print(f'Петя сделал {Petya}\nСережа сделал {Seryozha}\nКатя сделала {Katya}')

# Petya = 'x'
# Seryozha = 'x'
# Katya = '(х + x)*2 = 4х' 
# s = 'x + x + 4x'
# s = '6x'
# x = 's/6'
# x = 1