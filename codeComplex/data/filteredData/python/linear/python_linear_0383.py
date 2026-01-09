from math import gcd, sqrt, factorial, pi, inf
from collections import deque, defaultdict
from bisect import bisect, bisect_left
from time import time
from itertools import permutations as per
from heapq import heapify, heappush, heappop, heappushpop

N = 10**9 + 7
lcm = lambda x, y: (x * y) // gcd(x, y)
sm = lambda x: (x**2 + x) // 2


def main(n):
    # 生成与规模 n 对应的测试数据
    # 原程序需要 n, k 和 k 行 (x, d)
    # 这里设 k = n，并根据 i 构造 x, d
    k = n

    # 构造一组有正有负的 d，x 随 i 变化
    pairs = []
    for i in range(k):
        x = i + 1
        # 让 d 在负数和正数之间有规律变化
        d = (i % 5) - 2  # 取值范围：-2,-1,0,1,2
        if d == 0:
            d = 1
        pairs.append((x, d))

    s = 0
    for (x, d) in pairs:
        s += n * x
        if d < 0:
            s += sm(n // 2) * d + sm(n // 2 - (n + 1) % 2) * d

        else:
            s += sm(n - 1) * d

    # 保持与原代码相同的浮点输出行为
    result = s / n
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)