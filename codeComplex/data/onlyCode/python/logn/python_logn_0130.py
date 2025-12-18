from math import sqrt
n,k = map(int, input().split())

ub = k*(k+1)//2 - k+1

if n> ub:
    print(-1)
elif n == ub:
    print(k-1)
elif n == 1:
    print(0)
elif n<=k:
    print(1)
else:
    st = 1
    en = k-1
    target = n-1
    ub = k*(k-1)//2
    p = lambda x: ub - x*(x-1)//2
    ans = -1

    while st <= en:
        md = (st+en)//2
        if p(md) <= target:
            ans = md
            
            en = md-1
        else:
            st = md +1
    
    if p(ans) == target:
        print(k-ans)
    else:
        print(k-ans+1)
