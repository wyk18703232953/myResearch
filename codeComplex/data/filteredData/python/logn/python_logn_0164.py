#!/usr/bin/env python
from bisect import bisect, bisect_left, insort, insort_left
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from itertools import (
    accumulate, combinations, combinations_with_replacement, groupby,
    permutations, product)
from math import (
    acos, asin, atan, ceil, cos, degrees, factorial, hypot, log2, pi, radians,
    sin, sqrt, tan)
from operator import itemgetter, mul
from string import ascii_lowercase, ascii_uppercase, digits
import random


def getSum(p, q):
    n = q - p + 1
    temp = (n * (p + q) // 2) - n + 1
    return temp, n


def solve(n, k):
    l = 2
    r = k
    ans = -1

    while l <= r:
        mid = l + (r - l) // 2
        tot, count = getSum(mid, k)
        if tot >= n:
            ans = count
        if tot < n:
            r = mid - 1
        else:
            l = mid + 1
    if n == 1:
        ans = 0
    return ans


def main(scale_n):
    # 根据规模 scale_n 生成测试数据：
    # 令 k 为不小于 2 的整数，约与 scale_n 同阶
    k = max(2, scale_n)

    # n 的取值不超过 getSum(2, k) 的总和，避免无解区间
    max_tot, _ = getSum(2, k)
    n = random.randint(1, max_tot)

    ans = solve(n, k)
    print(ans)


if __name__ == "__main__":
    # 示例：使用某个规模调用 main
    main(10)