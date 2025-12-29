from bisect import bisect_right as lb
from collections import deque
from queue import PriorityQueue as pq
from math import *

mod = 10**9 + 7
inv = lambda x: pow(x, mod - 2, mod)

def solve(n, s):
    l = s
    h = n
    ans = n + 1

    while l <= h:
        m = (l + h) // 2

        t = 0
        for ch in str(m):
            t += int(ch)

        if m - t >= s:
            ans = m
            h = m - 1
        else:
            l = m + 1

    return n - ans + 1

def main(n):
    # 根据 n 生成测试数据
    # 原题逻辑需要两个参数 n, s
    # 这里令 s 为 1 到 n 之间的某个值（例如中间值）
    s = max(1, n // 2)

    result = solve(n, s)
    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自由调整
    main(10**6)