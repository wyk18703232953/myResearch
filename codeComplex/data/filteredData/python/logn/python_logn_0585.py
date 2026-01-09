import math
from functools import reduce
import operator as op
from math import gcd, inf, sqrt, pi, cos, sin, ceil, log2, floor, log
from bisect import bisect_right, bisect_left, bisect
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(2**20)

MOD = 1000000007
PMOD = 998244353
N = 10**18 + 1
LOGN = 30
alp = 'abcdefghijklmnopqrstuvwxyz'


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1

        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(factors)


def isPowerOfTwo(x):
    return x and (not (x & (x - 1)))


def main(n):
    # 生成测试数据：
    # 给定规模 n，构造 n 和 k
    # 示例策略：n 按参数给定，k 取 n 的一半（向下取整）
    k = n // 2

    det = int(sqrt(9 + 8 * (n + k)) - 3) // 2
    result = n - det
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用：规模为 10
    main(10)