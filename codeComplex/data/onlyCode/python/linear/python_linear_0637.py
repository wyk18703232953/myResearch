'''input
5
1 4 1 2 1
5
2 2 2 2 2

3
1 1 1
5
1 4 1 1 1

'''
n = int(input())
a = list(map(int, input().split()))
b = []
c = []
e = []
for i in range(n):
	if a[i] == 1:
		b += [i]
for i in range(n):
	if a[i] != 1:
		c += [[a[i], i]]
if not c:
	print("NO")
	exit(0)
ans = len(c)
for i in range(len(c) - 1):
	e += [(c[i][1], c[i + 1][1])]
	c[i][0] -= 1
	c[i + 1][0] -= 1
if b:
	e += [(b[-1], c[-1][1])]
	c[-1][0] -= 1
	b.pop()
	ans += 1
if b:
	e += [(b[-1], c[0][1])]
	c[0][0] -= 1
	b.pop()
	ans += 1
i = 0
while b:
	while i < len(c) and c[i][0] == 0:
		i += 1
	if i == len(c):
		print("NO")
		exit(0)
	e += [(b[-1], c[i][1])]
	c[i][0] -= 1
	b.pop()


print("YES", ans - 1)
print(len(e))
for (x, y) in e:
	print(x + 1, y + 1)
