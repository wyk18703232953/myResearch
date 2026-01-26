from math import log
n,k=map(int,input().split())
s=list(map(int,input().split()))
ans=0
for j in range(11):
    d=dict()
    z=10**j
    for i in s:
        y=i*z
        u=y%k
        if u in d:
            d[u]+=1
        else:
            d.update({u:1})
    for i in s:
        y=i
        lg=int(log(i,10))+1
        lg=10**lg
        if lg==z:
            d[(y*z)%k]-=1
            x=(k-y%k)
            if y%k==0:
                x=0
            if x in d:
                ans+=d[x]
            d[(y*z)%k]+=1 
print(ans)
