import sys
from math import sqrt, gcd, ceil, log, floor
from bisect import bisect, bisect_left
from collections import defaultdict, Counter, deque
from heapq import heapify, heappush, heappop

MOD = 10**9 + 7


def main(n):
    # n 表示每种颜色数组的长度规模，且不超过 200
    r = g = b = min(max(1, n), 200)
    r_ar = [i for i in range(r, 0, -1)]
    g_ar = [i * 2 for i in range(g, 0, -1)]
    b_ar = [i * 3 for i in range(b, 0, -1)]

    N = 201
    dp = [[[-1] * N for _ in range(N)] for _ in range(N)]

    def f(x, y, z):
        if ((x >= r) + (y >= g) + (z >= b)) >= 2:
            return 0
        if dp[x][y][z] != -1:
            return dp[x][y][z]
        maxi = 0
        if x < r and y < g:
            maxi = max(maxi, r_ar[x] * g_ar[y] + f(x + 1, y + 1, z))
        if z < b and y < g:
            maxi = max(maxi, b_ar[z] * g_ar[y] + f(x, y + 1, z + 1))
        if x < r and z < b:
            maxi = max(maxi, r_ar[x] * b_ar[z] + f(x + 1, y, z + 1))
        dp[x][y][z] = maxi
        return maxi

    # print(f(0, 0, 0))
    pass
if __name__ == "__main__":
    main(5)