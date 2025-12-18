n,k=map(int,input().split())
if k>n+(n-1):
    print(0)
else:
    if k<=n:
        print((k-1)//2)
    else:
        x=n-(k-n)
        print((x+1)//2)
