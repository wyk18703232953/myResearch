
import math

n, m = map(int, input().split())

b = list(map(int, input().split()))
g = list(map(int, input().split()))

first_max = 0
second_max = 0
for i in range(n):
	if b[i] < first_max and b[i] > second_max:
		second_max = b[i]
	if b[i] >= first_max:
		second_max = first_max
		first_max = b[i]

# print(first_max, second_max)
first_min = min(g)

if first_max > first_min:
	print(-1)
else:
	total = sum(b) * m + sum(g) - m * first_max + (first_max - second_max) * (first_min != first_max)
	print(total)
