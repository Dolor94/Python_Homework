number_ratings = int(input())
ratings = list(map(int, input().split()))
min = 1001
max = -1001
for x in ratings:
	if x > max:
		max = x
	elif x < min:
		min = x
for i in range(number_ratings):
	if ratings[i] == max:
		ratings[i] = min
print(*ratings)