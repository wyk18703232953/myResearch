MOD = 10 ** 9 + 7

x, k = map(int, input().split())
print(((2 * x - 1) * pow(2, k, MOD) + 1) % MOD if x else 0)
