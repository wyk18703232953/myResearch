from sys import stdin, stdout
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))

for _ in range(1):#nmbr()):
    n,m=lst()
    a=lst()
    a=[0]+a+[m]
    n=len(a)
    suf=[0]*n
    suf[n-2]=abs(a[-2]-a[-1])
    for i in range(n-3, -1, -1):
        suf[i]=a[i+1]-a[i]+suf[i+2]
    ans=suf[0]
    cost=0
    for i in range(1, n):
        if i&1:
            v=a[i]-1-a[i-1]
            if v!=0:ans=max(ans, cost+v+suf[i])
            cost+=a[i]-a[i-1]
        else:
            v=a[i-1]+1
            if v!=a[i]:ans=max(ans, cost+a[i]-v+(suf[i+1] if i+1<n else 0))
    print(ans)