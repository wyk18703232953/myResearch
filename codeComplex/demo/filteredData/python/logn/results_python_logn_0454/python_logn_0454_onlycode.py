import math

t = int(input())
res = []
while t:
	t -= 1
	n, k = map(int, input().split())
	limit = -1
	if n <= 60:
		limit = 0
		pow4 = 1
		for _ in range(n):
			limit += pow4
			pow4 *= 4
	if limit < k and limit != -1 or n == 2 and k == 3:
		res.append('NO')
	else:
		div = 1
		k -= 1
		size = 1
		while div < n and k >= 4 * size - 1:
			k -= 4 * size - 1
			size *= 2
			div += 1
		res.append('YES ' + str(n - div))

print('\n'.join(res))