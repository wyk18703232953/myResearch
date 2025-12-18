n = int(input())
ar = list(map(int, input().split()))
rev = ar[::-1]
from collections import Counter
def d(ar):
	me = Counter()
	s = 0 
	for i in range (n) : 
		s+=(i*ar[i])
		s-=(me[ar[i]] + me[ar[i]+1]*ar[i] + me[ar[i]-1]*ar[i])
		me[ar[i]]+=1
	return s
print(d(ar) - d(rev))