import sys
from functools import lru_cache, cmp_to_key
from heapq import merge, heapify, heappop, heappush
from collections import defaultdict as dd, deque, Counter as C
from itertools import combinations as comb, permutations as perm
from bisect import bisect_left as bl, bisect_right as br, bisect
from time import perf_counter
from fractions import Fraction
import copy
import time

mod = int(pow(10, 9) + 7)
mod2 = 998244353

def l1d(n, val=0):
    return [val for _ in range(n)]

def l2d(n, m, val=0):
    return [l1d(m, val) for _ in range(n)]

def pmat(A):
    for ele in A:
        print(*ele, end="\n")

def main(n):
    if n <= 0:
        return
    # 原程序结构：
    # n = L()[0]
    # A = sorted(L())
    # if A == [1]*n:
    #     print(*A[:n-1], 2)
    # else:
    #     print(1, *A[:-1])
    #
    # 这里将输入规模 n 解释为数组长度。
    # 构造一个确定性的长度为 n 的整数数组 A。
    # 使其既包含全为 1 的情况，也包含非全为 1 的情况可控。
    # 为时间复杂度实验，主要是 sorted 的 O(n log n)。

    # 确定性构造：前半部分为 1，后半部分为 i % 5 + 1
    A = [(1 if i < n // 2 else (i % 5 + 1)) for i in range(n)]

    # 保持和原逻辑一致：先排序
    A = sorted(A)

    if A == [1] * n:
        if n == 1:
            print(2)
        else:
            print(*A[:n-1], 2)
    else:
        if n == 1:
            print(1)
        else:
            print(1, *A[:-1])

if __name__ == "__main__":
    main(10)