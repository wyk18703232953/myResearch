d = {}
n = int(input())
for _ in range(n):
	a,x = map(int,input().split())
	d[a] = x
m = int(input())
for _ in range(m):
	b,y = map(int,input().split())
	if b in d:
		d[b] = max(y,d[b])
	else:
		d[b] = y
count = 0
for i in d:
	count += d[i]
print(count)