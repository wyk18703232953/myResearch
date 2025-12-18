n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
a.reverse()
b.reverse()
if a[0]>b[-1]:
    print(-1)
else:
    que=[]
    flag=True
    if b[-1]==a[0]:
        s=sum(b)
        flag=False
    else:
        s=sum(b)-b[-1]+a[0]
    if flag:
        s+=(sum(a)-a[0])*m+b[-1]-a[1]
    else:
        s+=(sum(a)-a[0])*m
    print(s)
