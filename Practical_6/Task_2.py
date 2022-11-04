# Пам-парам парам-пам парам

text = input().split()
set_1 = set()
for i in text:
    count = 0
    for j in i:
        if j.lower() in "ауоыиэяюёе":
            count += 1
    set_1.add(count)
if len(set_1) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")