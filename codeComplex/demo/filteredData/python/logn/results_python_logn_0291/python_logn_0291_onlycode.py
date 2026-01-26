mod = 1000000000 + 7

n, m = map(int, input().split())

if n == 0:
    print(0)
    exit()

ans = n * 2
ans %= mod

if m:
    t = 1
    x = 2
    while m > 0:
        if m & 1:
            t = t * x % mod
        x = x * x % mod
        m >>= 1
    ans -= 1
    ans = (t * ans + 1) % mod

print(ans)