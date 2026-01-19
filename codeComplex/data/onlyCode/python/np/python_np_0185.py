


from itertools import combinations

[n,l,r,x] = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
c.sort()
k = 0

from itertools import combinations

for i in range(n) :
	for j in range(i+1,n) :
		if ( c[j] - c[i] ) >= x :
			if sum(c[i:j+1]) < l :
				continue
			elif  (c[i] + c[j]) > r :
				continue
			else :
				if (c[i] + c[j]) >= l and (c[i] + c[j]) <= r :
					k += 1
				for p in range(1,j-i) :
					for m in combinations(c[i+1:j],p) :
						if (sum(m)+c[i] +c[j]) >= l and (sum(m)+c[i] +c[j]) <= r :
							k+=1
				
						
						


print(k)


