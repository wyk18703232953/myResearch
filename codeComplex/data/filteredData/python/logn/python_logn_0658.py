#!/usr/bin/env python
import os
import re
import sys
from bisect import bisect, bisect_left, insort, insort_left
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from fractions import gcd
from io import BytesIO, IOBase
from itertools import (
    accumulate, combinations, combinations_with_replacement, groupby,
    permutations, product)
from math import (
    acos, asin, atan, ceil, cos, degrees, factorial, hypot, log2, pi, radians,
    sin, sqrt, tan)
from operator import itemgetter, mul
from string import ascii_lowercase, ascii_uppercase, digits
import random


def getReamin(action, n):
    n -= action
    ans = (n * (n + 1) // 2) - action
    return ans


def solve(n, k):
    l = 1
    r = n
    res = 0
    while l <= r:
        mid = l + (r - l) // 2
        remain = getReamin(mid, n)
        if remain == k:
            res = mid
            break
        if remain > k:
            l = mid + 1
        else:
            r = mid - 1
    return res


def main(n):
    # 根据规模 n 生成测试数据
    # 约束：1 <= n，k 在 [0, n*(n+1)//2] 范围内
    if n <= 0:
        n = 1
    max_sum = n * (n + 1) // 2

    # 随机生成一个动作 action，使 remain 在合理范围内
    action = random.randint(1, n)
    k = getReamin(action, n)
    # 现在保证存在解 action，使得 getReamin(action, n) == k

    res = solve(n, k)
    print(res)


# region fastio (保留但不再使用 input())
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input():  # 不再在 main 中使用，仅为兼容保留
    return sys.stdin.readline().rstrip("\r\n")
# endregion


if __name__ == "__main__":
    # 示例：使用 n = 10 运行一次
    main(10)