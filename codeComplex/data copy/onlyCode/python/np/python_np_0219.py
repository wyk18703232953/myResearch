n,l,r,x = map(int,input().split())
c = list(map(int,input().split()))
res = 0
for i in range(1 << n):
	Bit = []
	for j in range(n):
		if i & (1 << j):
			Bit.append(c[j])
	if (len(Bit) >= 2) and (l<= sum(Bit) <= r) and (max(Bit) - min(Bit) >= x):
		res+= 1
print(res)