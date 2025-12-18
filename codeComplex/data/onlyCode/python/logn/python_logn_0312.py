def pow1(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    else:
        if k % 2 == 0:
            a = pow1(n, k // 2) % mod
            return a * a % mod
        else:
            return pow1(n, k - 1) % mod * n % mod

 
mod = 10 ** 9 + 7
n, k = map(int, input().split())
if n == 0:
    print(0)
else:
    x = pow1(2, k + 1) % mod
    print(((n * x - pow1(2, k) + 1)) % mod)