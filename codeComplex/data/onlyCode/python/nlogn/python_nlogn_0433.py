from collections import defaultdict
n=int(input())
a=list(map(int, input().split()))

d=defaultdict(int)
cnt=0

for i in range(n):
    d[a[i]]+=1

for i in range(n):
    f=0
    for j in range(1,31):
        p=2**j-a[i]
        if p<=0:
            continue
        if p!=a[i]:
            if d[p]>=1:
                f=1
        else:
            if d[p]>=2:
                f=1
    if not f:
        cnt+=1
print(cnt)
