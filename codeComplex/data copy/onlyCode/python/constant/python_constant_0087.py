import math
n = int(input())
m = 0
for i in range(min(100,n)):
	for ii in range(min(100,n)):
		for iii in range(min(100,n)):
			i1 = n-i
			ii1 = n-ii
			iii1 = n-iii
			r1 = (i1*ii1)//math.gcd(i1,ii1)
			r2 = (r1*iii1)//math.gcd(iii1,r1)
			m = max(m,r2)
print(m)