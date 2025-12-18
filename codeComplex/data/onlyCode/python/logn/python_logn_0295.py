x, k = map(int, input().split())
MOD = 10 ** 9 + 7

def get(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return (get(a, n - 1) * a) % MOD
    else:
        b = get(a, n // 2) % MOD
        return (b * b) % MOD

if x == 0:
    print(0)
else:
    print((x * get(2, k + 1) - get(2, k) + 1) % MOD)
