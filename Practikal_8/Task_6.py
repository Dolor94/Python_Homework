# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.

import random

coins = int(input("Введите число монеток: "))
print(f"Число монеток = {coins}")
list = [random.randint(0, 1) for i in range(coins)]
print(*list)
eagle = 0
nut = 0
score = 0 
while score < len(list):
    if list[score] == 0:
        eagle += 1
    elif list[score] == 1:
        nut += 1
    score += 1
print(f"{eagle if eagle < nut else nut} - это минимальное число монеток, которые нужно перевернуть")
