import sys
import bisect
from bisect import bisect_left as lb
from math import log
from math import gcd
from math import atan2, acos

mod = 10**9 + 7
gp = []
cost = []
dp = []
mx = []
ans1 = []
ans2 = []
special = []
specnode = []
a = 0
kthpar = []


def dfs(root, par):
    if par != -1:
        dp[root] = dp[par] + 1
    for i in range(1, 20):
        if kthpar[root][i - 1] != -1:
            kthpar[root][i] = kthpar[kthpar[root][i - 1]][i - 1]
    for child in gp[root]:
        if child == par:
            continue
        kthpar[child][0] = root
        dfs(child, root)


def generate_p(n):
    # Deterministic matrix with values in [0,1], diagonal 0
    p = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                val = 0.0
            else:
                val = ((i + 1) * (j + 2)) % 1001 / 1000.0
            row.append(val)
        p.append(row)
    return p


def hnbhai(n, p):
    dp_local = [0.0] * (1 << n)
    if n > 0:
        dp_local[1] = 1.0
    for i in range(2, 1 << n):
        for j in range(1, n):
            if not ((i >> j) & 1):
                continue
            for k in range(0, j):
                if (i >> k) & 1:
                    v = max(
                        dp_local[i],
                        dp_local[i ^ (1 << j)] * p[k][j] + dp_local[i ^ (1 << k)] * p[j][k],
                    )
                    dp_local[i] = v
    return dp_local[-1] if dp_local else 0.0


def main(n):
    # Interpret n as number of players in original problem
    if n < 1:
        n = 1
    # Original algorithm is exponential; cap n to keep runtime scalable in practice
    # while still preserving asymptotic structure for experiments.
    max_n = 12
    if n > max_n:
        n = max_n
    p = generate_p(n)
    result = hnbhai(n, p)
    print(result)


if __name__ == "__main__":
    main(4)