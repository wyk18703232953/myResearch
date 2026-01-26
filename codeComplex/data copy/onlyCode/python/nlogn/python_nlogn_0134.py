n,m,k=map(int,input().split())
x=list(map(int,input().split()))
x.sort(reverse=True)
i=-1
if k>=m:
    print(0)
else:
    for i in range(n):
        k-=1
        k+=x[i]
        if k>=m:
            break
    if k>=m:
        print(i+1)
    else:print(-1)