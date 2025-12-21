import sys
from array import array
import random

def main(n):
    random.seed(0)
    edge = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    mod = 10**9 + 7

    dp_f = [[-1] * n for _ in range(n)]
    dp_g = [[-1] * n for _ in range(n)]

    for i in range(n):
        dp_f[i][i] = 1
        dp_g[i][i] = 1
    for i in range(n - 1):
        val = 1 if edge[i][i + 1] else 0
        dp_f[i][i + 1] = val
        dp_g[i][i + 1] = val

    sys.setrecursionlimit(10**7)

    def f(l, r):
        if dp_f[l][r] != -1:
            return dp_f[l][r]
        dp_f[l][r] = g(l, r) if edge[l][r] else 0
        for m in range(l + 1, r):
            if edge[l][m]:
                dp_f[l][r] = (dp_f[l][r] + g(l, m) * f(m, r)) % mod
        return dp_f[l][r]

    def g(l, r):
        if dp_g[l][r] != -1:
            return dp_g[l][r]
        dp_g[l][r] = f(l + 1, r)
        for m in range(l + 1, r):
            dp_g[l][r] = (dp_g[l][r] + f(l, m) * f(m + 1, r)) % mod
        return dp_g[l][r]

    return f(0, n - 1)

if __name__ == "__main__":
    print(main(5))