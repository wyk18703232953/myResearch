"""
NTC here
"""
from sys import setcheckinterval,stdin
setcheckinterval(1000)

#print("Case #{}: {} {}".format(i, n + m, n * m))

iin=lambda :int(stdin.readline())
lin=lambda :list(map(int,stdin.readline().split()))

n,q=lin()
a=lin()
if q==0:
    exit()
Q=[iin() for i in range(q)]
sq=set(Q)
mx=max(Q)
d=dict()
ch=1
for i in range(min(mx,n+1)):
    if ch==n:
        ch=1
    if i+1 in sq:d[i+1]=[a[0],a[ch]]
    if a[0]<a[ch]:
        a[0],a[ch]=a[ch],a[0]
    ch+=1

for i in Q:
    if i>n:
        x=n-1 if i%(n-1)==0 else i%(n-1)
        print(a[0],a[x])
    else:
        print(*d[i])




