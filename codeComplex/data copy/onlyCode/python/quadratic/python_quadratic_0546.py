def stones_after(n, s):
	for i in s:
		if i == '-':
			n -= 1
		else:
			n += 1
		if n < 0:
			return -1
	return n

n = int(input().strip())
s = input().strip()
ans = 99999999
for i in range(n+1):
	stones = stones_after(i, s)
	if stones != -1:
		ans = min(ans, stones)
print(ans)