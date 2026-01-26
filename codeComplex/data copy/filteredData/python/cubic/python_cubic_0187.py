from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

mod = 998244353
INF = float('inf')


def comb(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0


def perm(n, m):
    return factorial(n) // (factorial(n - m)) if n >= m else 0


def mdis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main(n):
    # n: problem size; also length of generated array
    if n <= 0:
        return 0

    # Deterministic array generation of length n
    # Values are small positive integers, patterned but fixed for given n
    arr = [(i % 3) + 1 for i in range(n)]

    dp = [[n] * n for _ in range(n)]
    rec = [[0] * n for _ in range(n)]

    for i in range(n):
        rec[i][i] = arr[i]
        dp[i][i] = 1

    for le in range(2, n + 1):
        for l in range(n):
            r = l + le - 1
            if r > n - 1:
                break
            for m in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][m] + dp[m + 1][r])

                if rec[l][m] == rec[m + 1][r] and dp[l][m] == dp[m + 1][r] == 1:
                    dp[l][r] = 1
                    rec[l][r] = rec[l][m] + 1

    result = dp[0][-1]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call; change n as needed for experiments
    main(10)