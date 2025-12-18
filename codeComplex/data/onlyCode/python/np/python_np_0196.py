kk=lambda:map(int, input().split())
ll=lambda:list(kk())
n,l,r,d=kk()
p,t=ll(),0
for v in range(2**n):
	s = []
	for i in range(n):
		if v&(2**i):
			s.append(p[i])
	if l <= sum(s)<=r and max(s)-min(s) >= d: t+=1
print(t)