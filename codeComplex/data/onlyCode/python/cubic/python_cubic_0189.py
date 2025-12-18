n = int(input())
b = list(map(int, input().split(' ')))
e = [[-1] * (n+1) for _ in range(2048)]
 
d = [[] for _ in range(n)]
for i, v in enumerate(b):
	e[v][i] = i
	d[i].append(i)
 
for v in range(1, 2048):
	for i in range(n):
		j = e[v][i]
		if j != -1:
			h = e[v][j+1]
		else:
			h = -1
		if j != -1 and h != -1:
			e[v+1][i] = h
			d[i].append(h)
 
a = [_ for _ in range(1, n+1)]
for s in range(n):
	for e in d[s]:
		if s > 0:
			temp = a[s-1]+1
		else :
			temp = 1
		a[e] = min(a[e], temp)
print(a[n-1])