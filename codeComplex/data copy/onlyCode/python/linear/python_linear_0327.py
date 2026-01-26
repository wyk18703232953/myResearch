n,M=map(int,input().split())
a=[0]+[int(x) for x in input().split()]+[M]

t1=[]
t2=[]
for i in range(n+1):
    if i%2==0:
        t1.append(a[i+1]-a[i])
    else:
        t2.append(a[i+1]-a[i])
t2.append(0)

import math
ans=sum(t1)
p=0
q=sum(t2)
for i in range(math.ceil(n/2)):
    p=p+t1[i]
    q=q-t2[i-1]
    ans=max(ans,p+q-1)
print(ans)
