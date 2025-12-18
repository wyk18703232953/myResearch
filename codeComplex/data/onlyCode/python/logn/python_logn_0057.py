ii=lambda:int(input())
kk=lambda:map(int, input().split())
ll=lambda:list(kk())

from math import log
l,r=kk()
i=msb = int(max(log(l,2),log(r,2)))
while ((2**i)&l) == ((2**i)&r):
	i-=1
	if i == -1:
		break
i+=1
print(2**i-1)