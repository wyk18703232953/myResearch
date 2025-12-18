from math import *
from collections import *
n = int(input())
a = list(map(int,input().split()))
d = Counter(a)
ans = 0
for i in range(n):
    for j in range(31):
        s = 2**j
        s = s-a[i]
        if d.get(s)!=None and ((d[s]==1 and s!=a[i]) or d[s]>=2):
            break
    else:
        ans+=1
print(ans)