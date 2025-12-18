n,k = map(int,input().split())
if k>n+n-1:
    print(0)
    exit(0)
if k-1<=n:
    ml = 1
    mr = k-1
    print((mr-ml+1)//2)
else:
    mr = n
    ml = k-n
    print((mr-ml+1)//2)