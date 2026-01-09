import sys
from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

mod = 998244353
INF = float('inf')


def comb(n, m): return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0
def perm(n, m): return factorial(n) // (factorial(n - m)) if n >= m else 0
def mdis(x1, y1, x2, y2): return abs(x1 - x2) + abs(y1 - y2)


def main(n):
    # n controls the scale: number of distinct CDs and also bounds k, list lengths, etc.
    if n <= 0:
        # print(0)
        pass
        return

    # Make k depend on n but stay reasonably small relative to n to control dp size
    k = max(1, n // 3)

    # cds: list of length n*k, values in [1, n]
    cds = [(i % n) + 1 for i in range(n * k)]

    # fn: list of length n, values in [1, n]
    fn = [(i * 2) % n + 1 for i in range(n)]

    # sc: list of length k+1, sc[0] = 0
    sc = [0] + [i for i in range(1, k + 1)]

    rec = set(fn)
    uses = 0
    dic = defaultdict(int)
    for i in cds:
        if i in rec:
            dic[i] += 1
            uses += 1

    dp = [[0] * (n * k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n * k + 1):
            for l in range(k + 1):
                if l > j:
                    break
                val = sc[l]
                dp[i][j] = max(dp[i][j], dp[i - 1][j - l] + val)

    res = 0
    for i, v in Counter(fn).items():
        res += dp[v][dic[i]]

    # print(res)
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)