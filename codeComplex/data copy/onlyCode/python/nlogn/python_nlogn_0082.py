from sys import stdin,stdout
nmbr=lambda:int(stdin.readline())
lst = lambda: list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr()):
    n,k=lst()
    a=sorted([lst() for _ in range(n)],key=lambda x:(-x[0],x[1]))
    p,t=-1,-1;ans=0
    if k<=n:p,t=a[k-1]
    for x,y in a:
        if x==p and y==t:ans+=1
    print(ans)