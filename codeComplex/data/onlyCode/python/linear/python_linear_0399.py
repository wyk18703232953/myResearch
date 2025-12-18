n=int(input())
m=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
curr=m
f=0
if b[0]!=1:
    curr+=(curr)/(b[0]-1)
else:
    f=1
for i in range(n-1,-1,-1):
    if a[i]!=1:
        curr+=(curr)/(a[i]-1)
    else:
        f=1
    if i>0:
        if b[i]!=1:
            curr+=(curr)/(b[i]-1)
        else:
            f=1
if f:
    print(-1)
else:
    print(curr-m)
