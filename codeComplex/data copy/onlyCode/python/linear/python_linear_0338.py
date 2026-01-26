from sys import stdin,stdout
nmbr=lambda:int(stdin.readline())
lst=lambda:list(map(int,stdin.readline().split()))
for _ in range(1):#nmbr())
    n,d=lst()
    a=sorted(lst())
    s=set()
    for i in range(n):
        x=a[i]-d
        left=a[i-1] if i>=1 else float('inf')
        if abs(x-left)>=d:s.add(x)
        x=a[i]+d
        right=a[i+1] if i+1<n else float('inf')
        if abs(x-right)>=d:s.add(x)
    print(len(s))