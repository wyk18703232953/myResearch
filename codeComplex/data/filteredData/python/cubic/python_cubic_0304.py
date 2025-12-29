import random
from math import sqrt, gcd, ceil, log, floor
from bisect import bisect, bisect_left
from collections import defaultdict, Counter, deque
from heapq import heapify, heappush, heappop

MOD = 10**9 + 7


def main(n):
    """
    n 为规模参数，用来生成测试数据：
    - r = g = b = n
    - 三个数组长度均为 n，元素为 1~10^4 的随机整数
    """

    r = g = b = n
    # 生成测试数据
    r_ar = sorted([random.randint(1, 10**4) for _ in range(r)], reverse=True)
    g_ar = sorted([random.randint(1, 10**4) for _ in range(g)], reverse=True)
    b_ar = sorted([random.randint(1, 10**4) for _ in range(b)], reverse=True)

    # dp 的维度为 (r+1) * (g+1) * (b+1)
    # 原代码是固定 N = 201，这里按 n 自适应，但为了避免过大内存，
    # 若 n > 200，仍限制为 201（可按需求修改）
    max_dim = min(n, 200) + 1
    dp = [[[-1] * max_dim for _ in range(max_dim)] for _ in range(max_dim)]

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

    ans = f(0, 0, 0)
    print(ans)


# 示例调用（实际评测系统可直接调用 main(n)）
if __name__ == "__main__":
    main(5)