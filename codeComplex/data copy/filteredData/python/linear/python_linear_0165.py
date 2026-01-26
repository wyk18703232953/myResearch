import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from math import *
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time

mod = int(pow(10, 9) + 7)
mod2 = 998244353

def out(*var, end="\n"):
    sys.stdout.write(' '.join(map(str, var)) + end)

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(n, val) for _ in range(m)]

def main(n):
    # 保持与原程序一致：n 是唯一输入规模
    if n < 6:
        # print(-1)
        pass

    else:
        # print(1, 2)
        pass
        # print(1, 3)
        pass
        # print(1, 4)
        pass
        for i in range(5, n + 1):
            # print(2, i)
            pass
    for i in range(1, n):
        # print(i, i + 1)
        pass
if __name__ == "__main__":
    # 示例：以 n=10 作为规模进行一次运行
    main(10)