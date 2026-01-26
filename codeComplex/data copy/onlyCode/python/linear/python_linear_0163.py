from math import gcd
from collections import defaultdict as dd
m=int(input())
d=dd(int)
l=[]
ans=[]
for i in range(m):
    s=input().split()[0]
    a=0
    b=0
    c=0
    n=len(s)
    ind=0
    for i in range(1,n):
        if(s[i]=='+'):
            ind=i+1
            break
        a=a*10+int(s[i])
    for i in range(ind,n):
        if(s[i]==')'):
            ind1=i+2
            break
        b=b*10+int(s[i])
    for i in range(ind1,n):
        c=c*10+int(s[i])
    a=a+b
    g=gcd(a,c)
    a=a//g
    c=c//g
    d[(a,c)]+=1
    l.append((a,c))
for i in l:
    ans.append(d[i])
print(*ans)