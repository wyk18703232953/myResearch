casas, tubos = map(int, input().strip().split())

def bs(c, t):
    l, r = 0, t-1
    while l <= r:
        mid = l+r >> 1
        if ((2*t - mid - 1)*mid)//2+1 < c:
            l = mid+1
        else:
            r = mid-1
    return r+1

res = bs(casas, tubos)
print(-1 if res == tubos else res)    
    
