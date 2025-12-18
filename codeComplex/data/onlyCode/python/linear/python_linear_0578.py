n = int(input())
res = []
multiplier = 1
while n > 1:
	new_n = n // 2
	res.extend((multiplier,)*(n-new_n))
	if n == 3:
		multiplier *= 3
	else:
		multiplier *= 2
	n = new_n
res.extend((multiplier,)*n)
print(*res)
