x, k = map(int, input().split())
mod = 10**9+7
e = (x * pow(2, k, mod)) % mod
s = (e - pow(2, k, mod)) % mod
f = lambda x: (x*(x+1))%mod
ans = ((f(e) - f(s)) * pow(2, k*(mod-2), mod))%mod
print(ans if x != 0 else 0)