MOD = int(1e9 + 7)
x, k = map(int, input().split())
if x == 0: print(0)
else: print((x * pow(2, k+1, MOD) - pow(2, k, MOD) + 1) % MOD)