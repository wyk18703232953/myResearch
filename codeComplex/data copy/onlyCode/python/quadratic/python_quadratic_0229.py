import math
import sys

n=int(input())
s=list(map(int,input().split()))
ce=list(map(int,input().split()))

best=10**9
for j in range(1,n-1):
    a=ce[j];b=10**9;c=10**9
    for i in range(j-1,-1,-1):
        if s[i]<s[j]:
            b=min(b,ce[i])
    for k in range(j+1,n):
        if s[k]>s[j]:
            c=min(c,ce[k])
    best=min(best,a+b+c)

if best>=10**9:
    print(-1)
else:
    print(best)