# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

number = int(input("Введите число: "))
score = 1
sum = 0
while score <= number:
    sum += score
    score += 1
print(sum)