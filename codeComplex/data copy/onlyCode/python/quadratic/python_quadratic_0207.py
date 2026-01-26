n, m = map(int, input().split())
x = list(list(map(int , input())) for i in range(n))
res = [0] * m
for i in range(n):
	for j in range(m):
		res[j] += x[i][j]

for i in range(n):
	ok = 1
	for j in range(m):
		if res[j] == 1 and x[i][j] == 1:
			ok = 0
			break
	if ok:
		print("YES")
		exit()
print("NO")
