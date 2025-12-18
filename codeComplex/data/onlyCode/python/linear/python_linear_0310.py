from collections import defaultdict
import sys
import bisect
input=sys.stdin.readline

n,m=map(int,input().split())
a=[int(i) for i in input().split()if i!='\n']
rem=[[] for i in range(m)]
req=n//m
ans=0
for i in range(n):
    rem[a[i]%m].append([a[i],i])
ind=m-1
for i in range(m):
    size=len(rem[i])
    if size>req:
        ind=i
    if size<req:
        ok=False
        for j in range(ind,ind-m,-1):
            while len(rem[j])>req:
                pop,_=rem[j].pop()
                rem[i].append([pop+(i-j)%m,_])
                if len(rem[i])==req:
                    ok=True
                    break
            if ok:
                break
            ind-=1
            
out=[0]*(n)
for i in rem:
    for j in i:
        out[j[1]]=j[0]
print(sum(out)-sum(a))
out=' '.join(map(str,out))
print(out)
                    
                
    
        
        
    
        
    
    
