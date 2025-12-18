n, m = map(int, input().split())
c = list(map(int, input().split()))
a = list(map(int, input().split()))

x = 0
for i in range(n):
	try:
		if a[0] >= c[i]:
			x += 1
			a.pop(0)
	except IndexError:
		pass

print(x)