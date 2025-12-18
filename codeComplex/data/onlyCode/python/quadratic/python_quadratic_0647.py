n = int(input())
a = list(map(int, input().split()))

a.sort()
ans = 0
while a:
	m = a[0]
	b = []
	for x in a[1:]:
		if x % m != 0:
			b.append(x)
	a = b
	ans += 1
print(ans)