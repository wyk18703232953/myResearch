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
    return [l1d(m, val) for _ in range(n)]

def pmat(A):
    for ele in A:
        # print(*ele, end="\n")
        pass

def seive():
    prime = [1 for _ in range(10**6 + 1)]
    prime[0] = 0
    prime[1] = 0
    for i in range(10**6 + 1):
        if prime[i]:
            for j in range(2 * i, 10**6 + 1, i):
                prime[j] = 0
    return prime

def rec(a, b):
    if b == 1:
        return a
    if a > b:
        return a // b + rec(b, a % b)

    else:
        return rec(b, a)

def main(n):
    # 输入结构为两个整数 a, b
    # 将规模 n 映射为：
    # a = n + 1, b = n + 2，保证 a < b 且 b != 0、1 对大多数 n 成立
    if n < 1:
        a, b = 1, 2

    else:
        a = n + 1
        b = n + 2
        if b == 1:
            b = 2
    result = rec(a, b)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)