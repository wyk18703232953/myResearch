import math
x, k = list(map(int, input().split()))
mod = 10**9 + 7
print((pow(2, k+1, mod)*x - pow(2, k, mod) + 1) % mod if x > 0 else 0)
