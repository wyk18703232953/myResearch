x, k = (int(x) for x in input().split())
mod = 10**9 + 7
if x == 0:
    print(0)
    quit()
if k == 0:
    print(x * 2 % mod)
    quit()
ans = pow(2, k + 1, mod)
ans *= x
ans %= mod
ans -= pow(2, k, mod) - 1
ans %= mod
ans += mod
ans %= mod
print(ans)
