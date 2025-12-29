from math import ceil, sqrt, log, gcd
from heapq import heappush, heappop
from functools import cmp_to_key as ctk
from collections import deque, defaultdict as dd
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
import random

abc = 'abcdefghijklmnopqrstuvwxyz'
mod = 998244353
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def sod(n: int) -> int:
    s = 0
    while n:
        s += (n % 10)
        n //= 10
    return s


def solve_single(n: int, s: int) -> int:
    def fun(mid: int) -> bool:
        return mid - sod(mid) >= s

    l = 0
    r = n
    ans = -1
    while l <= r:
        m = l + (r - l) // 2
        if fun(m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    if ans == -1:
        ans = n + 1
    return n - ans + 1


def main(n: int):
    """
    n: 规模参数，用于生成测试数据。
       这里将原代码中的 n 上界设置为 10^n，
       s 在 [0, n] 中随机生成。
    """
    # 生成测试数据
    max_n = 10 ** n
    s = random.randint(0, n)

    # 调用原逻辑
    ans = solve_single(max_n, s)

    # 输出结果
    print(ans)


if __name__ == "__main__":
    # 示例：规模参数为 3，则 n=10^3，s∈[0,3]
    main(3)