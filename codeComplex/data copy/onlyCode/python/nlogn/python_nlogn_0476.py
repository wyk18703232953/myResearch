from collections import Counter

n,k=list(map(int,input().split()))
x=list(map(int,input().split()))

dd=Counter()
for i in range(k):
   
    dd[x[i]]=dd[x[i]]+1

 
final=0   
for i in range(1,k+1):
    ans=0
    d=dd.copy()
    for j in range(n):
        for jj in d:
            if d[jj]>=i:
                d[jj]-=i
                ans=ans+1
                break
    if ans>=n:
        final=i
    else:
        break
print(final)