'''input
6
10 2 3 5 4 2


'''
import sys
from collections import defaultdict as dd

mod=10**9+7

def ri(flag=0):
	if flag==0:
		return [int(i) for i in sys.stdin.readline().split()]
	else:
		return int(sys.stdin.readline())


n = ri(1)
a= ri()

b= sorted(a)
c= dd(int)


ans = 0
val=0
for i in range(n):
	if c[b[i]]==0:
		val+=1
		for j in range(n):
			if b[j]%b[i]==0:
				c[b[j]]=val

for i in c:
	ans = max(ans , c[i])

print(ans)

