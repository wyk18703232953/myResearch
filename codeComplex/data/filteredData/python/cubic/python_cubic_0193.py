#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import itertools, math

sqrt = math.sqrt
mod = 1000000007
inf = float('INF')

def solve_from_array(a):
    n = len(a)
    dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        dp[i][i + 1] = [a[i], a[i], 1]
        dp[i + 1][i] = [a[i], a[i], 1]
    for length in range(2, n + 1):
        for l in range(n - length + 1):
            tmp = [-inf, inf, inf]
            r = l + length
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

def main(n):
    # n controls the size of the input: length of the array
    # Deterministic construction of the array a of length n
    # Values are small integers with a simple repeating pattern
    a = [(i % 5) + 1 for i in range(n)]
    result = solve_from_array(a)
    # print(result)
    pass
if __name__ == "__main__":
    # Example: run with a specific n for experiment; adjust as needed
    main(10)