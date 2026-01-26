n=int(input())
c=0
for j in range(2,1+n//2):
	e=0
	i=n//j
	e+=(i*(i+1))//2
	e-=1
	if e>0:
		c+=e
print(c*4)