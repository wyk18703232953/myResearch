#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, itertools, math
sys.setrecursionlimit(10**5)

mod = 1000000007
inf = float('INF')

def solve_with_array(a):
    n = len(a)
    dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = [a[i], a[i], 1]
        dp[i + 1][i] = [a[i], a[i], 1]
    for i in range(2, n + 1):
        for l in range(n - i + 1):
            tmp = [-inf, inf, inf]
            r = l + i
            dpl = dp[l]
            dpr = dp[r]
            for m in range(l + 1, r):
                lm = dpl[m]
                mr = dpr[m]
                lr = lm[2] + mr[2] - (lm[1] == mr[0])
                if lr < tmp[2]:
                    tmp[2] = lr
                    if lm[1] == mr[0]:
                        if lm[2] == 1:
                            tmp[0] = lm[0] + 1
                        else:
                            tmp[0] = lm[0]
                        if mr[2] == 1:
                            tmp[1] = mr[1] + 1
                        else:
                            tmp[1] = mr[1]
                    else:
                        tmp[0] = lm[0]
                        tmp[1] = mr[1]
            dp[l][r] = tmp
            dp[r][l] = tmp
    return dp[0][n][2]

def generate_test_data(n):
    # 生成规模为 n 的测试数组 a
    # 这里生成 1..3 范围的整数，可按需要调整
    import random
    random.seed(0)
    return [random.randint(1, 3) for _ in range(n)]

def main(n):
    a = generate_test_data(n)
    ans = solve_with_array(a)
    print(ans)

if __name__ == '__main__':
    # 示例：调用 main(5)
    main(5)