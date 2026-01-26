x, k = map(int, input().split())
mod = 10**9+7
if x==0:
    print(0)
else:
    p = pow(2, k, mod)
    res = (((2*x)%mod + mod - 1)%mod)
    res = ((res*p)%mod + 1)%mod
    print(res)
