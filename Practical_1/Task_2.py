import os


# задача 2. Напишите программу для. 
# проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def clear(): return os.system("cls")
clear()
print("Проверка истинности утверждения: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

def user_XYZ(x):
    user_numbers = ["X", "Y", "Z"]
    arr = []
    for i in range(x):
        arr.append(int(input(f"Введите значение {user_numbers[i]}: ")))
    return arr

def checking(x):
    left = not(x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and x[2]
    result = left == right
    return result

answer = user_XYZ(3)

if checking(answer):
    print(f"¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z: Утверждение истинно")
else:
    print(f"¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z: Утверждение ложно")
