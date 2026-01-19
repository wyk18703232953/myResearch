import math as mt
import itertools as it
n,l,r,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for j in range(2,n+1):
    for i in it.combinations(a,j):
        if max(i)-min(i)>=x and l<=sum(i)<=r:
            ans+=1
print(ans)