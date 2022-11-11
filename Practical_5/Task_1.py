import os
from random import randint


# задача 1. Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота
# а) Подумайте как наделить бота ""интеллектом""

def clear(): return os.system("cls")
clear()
def player_vs_player():
    total_candies = 2021
    max_take_in_one_move_in_one_move = 28
    score = 0
    player_1 = input("Имя первого игрока?: ")
    player_2 = input("Имя второго игрока?: ")

    print("Опеределие чей ход будет первым...")

    x = randint(1, 2)
    if x == 1:
        first_move = player_1
        second_move = player_2
    elif x == 2:
        first_move = player_2
        second_move = player_1
    print(f"{first_move} ходит первым!")

    while total_candies > 0:
        if score == 0:
            step = int(input(f"\n {first_move}, сколько конфет Вы возьмёте: "))
            if step > total_candies or step > max_take_in_one_move_in_one_move:
                step = int(input(
                    f"\nМожно взять только {max_take_in_one_move_in_one_move} конфет, попробуйте еще раз: "))
            total_candies = total_candies - step
        if total_candies > 0:
            print(f"\nОсталось {total_candies} конфет!")
            score = 1
        else:
            print("Конфет больше нет!")

        if score == 1:
            step = int(
                input(f"\n {second_move}, сколько конфет Вы возьмёте: "))
            if step > total_candies or step > max_take_in_one_move_in_one_move:
                step = int(input(
                    f"\nМожно взять только {max_take_in_one_move_in_one_move} конфет, попробуйте еще раз: "))
            total_candies = total_candies - step
        if total_candies > 0:
            print(f"\nОсталось {total_candies} конфет!")
            score = 0
        else:
            print("Конфет больше нет!")

    if score == 1:
        print(f"{second_move} одрежал/а победу, поздралвяем!!!")
    if score == 0:
        print(f"{first_move} одрежал/а победу, поздралвяем!!!")


def player_vs_bot():
    total_candies = 2021
    max_take_in_one_move = 28
    player_1 = input("\nКак Вас зовут?: ")
    bot = "Компьютер"
    players = [player_1, bot]

    print("Опеределие чей ход будет первым...")

    first_move = randint(-1, 0)

    print(f"{players[first_move+1]} ходит первым !")

    while total_candies > 0:
        first_move += 1

        if players[first_move % 2] == "Компьютер":
            print(
                f"\nОсталось {total_candies} конфет \nХодит {players[first_move%2]}: ")

            if total_candies < 29:
                step = total_candies
            else:
                delenie = total_candies // 28
                step = total_candies - ((delenie*max_take_in_one_move)+1)
                if step == -1:
                    step = max_take_in_one_move - 1
                if step == 0:
                    step = max_take_in_one_move
            while step > 28 or step < 1:
                step = randint(1, 28)
            print(step)
        else:
            step = int(input(
                f"\nОсталось {total_candies} конфет \n{players[first_move%2]} сколько конфет Вы возьмёте: "))
            while step > max_take_in_one_move or step > total_candies:
                step = int(input(
                    f"\nМожно взять только {max_take_in_one_move} конфет, попробуйте еще раз: "))
        total_candies = total_candies - step

    print(
        f"Осталось {total_candies} конфет \n{players[first_move%2]} одрежал/а победу, поздралвяем!!!")

player_vs_player()
player_vs_bot()