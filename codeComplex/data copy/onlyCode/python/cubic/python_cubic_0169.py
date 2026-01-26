n= int(input())
b = [int(_) for _ in input().split()]
d = [[-1 if i != j else b[i] for i in range(n)] for j in range(n)]
for l in range(1, n):
	for s in range(n-l):
		e = s + l
		for m in range(s, e):
			if d[s][m] == d[m+1][e] and d[s][m] != -1:
				d[s][e] = d[s][m] + 1
a = [1]
for e in range(1, n):
	t = 4096
	for s in range(e+1):
		if d[s][e] != -1:
			t = min(t, ((a[s-1]+1) if s > 0 else a[s]))
	a.append(t)
print(a[-1])
