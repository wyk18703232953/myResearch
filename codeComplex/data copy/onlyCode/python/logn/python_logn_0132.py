n, k=[int(v) for v in input().split()]
if n==1:
    print(0)
elif n-1>(1+k-1)*(k-1)//2:
    print(-1)
else:
    n-=1
    k-=1
    l, r=0, k+1
    while r-l>1:
        m=(l+r)//2
        if (m+k)*(k-m+1)//2>=n:
            l=m
        else:
            r=m
    print(k-l+1)