import sys
import math
from fractions import Fraction
import collections
from itertools import permutations
from collections import defaultdict, deque
import threading

MOD = 10**9 + 7
omod = 998244353

class SegmentTree:
    def __init__(self, data, default=0, func=lambda a, b: a + b):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class SegmentTree1:
    def __init__(self, data, default=10**6, func=lambda a, b: min(a, b)):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        if start == stop:
            return self.__getitem__(start)
        stop += 1
        start += self._size
        stop += self._size
        res = self._default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)


class Factorial:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorials = [1, 1]
        self.invModulos = [0, 1]
        self.invFactorial_ = [1, 1]

    def calc(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.factorials):
            return self.factorials[n]
        nextArr = [0] * (n + 1 - len(self.factorials))
        initialI = len(self.factorials)
        prev = self.factorials[-1]
        m = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = prev * i % m
        self.factorials += nextArr
        return self.factorials[n]

    def inv(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        p = self.MOD
        pi = n % p
        if pi < len(self.invModulos):
            return self.invModulos[pi]
        nextArr = [0] * (n + 1 - len(self.invModulos))
        initialI = len(self.invModulos)
        for i in range(initialI, min(p, n + 1)):
            nxt = -self.invModulos[p % i] * (p // i) % p
            self.invModulos.append(nxt)
        return self.invModulos[pi]

    def invFactorial(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        if n < len(self.invFactorial_):
            return self.invFactorial_[n]
        self.inv(n)
        nextArr = [0] * (n + 1 - len(self.invFactorial_))
        initialI = len(self.invFactorial_)
        prev = self.invFactorial_[-1]
        p = self.MOD
        for i in range(initialI, n + 1):
            prev = nextArr[i - initialI] = (prev * self.invModulos[i % p]) % p
        self.invFactorial_ += nextArr
        return self.invFactorial_[n]


class Combination:
    def __init__(self, MOD):
        self.MOD = MOD
        self.factorial = Factorial(MOD)

    def ncr(self, n, k):
        if k < 0 or n < k:
            return 0
        k = min(k, n - k)
        f = self.factorial
        return f.calc(n) * f.invFactorial(max(n - k, k)) * f.invFactorial(min(k, n - k)) % self.MOD


prime = [True for _ in range(10)]
pp = [0] * 10


def SieveOfEratosthenes(n=10):
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p, n + 1, p):
                pp[i] += 1
                prime[i] = False
        p += 1


def binarySearch(arr, n, key):
    left = 0
    right = n - 1
    mid = 0
    res = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid][0] > key:
            right = mid - 1

        else:
            res = mid
            left = mid + 1
    return res


def run_algorithm(n_rows, m_cols, k_steps, r, c):
    n = n_rows
    m = m_cols
    k = k_steps
    if k % 2:
        for _ in range(n):
            # print(*([-1] * m))
            pass
        return
    dp = [[[0 for _ in range((k // 2) + 1)] for _ in range(m)] for _ in range(n)]
    for x in range(1, (k // 2) + 1):
        for i in range(n):
            for j in range(m):
                mn = 10**8
                if i > 0:
                    mn = min(mn, c[i - 1][j] + dp[i - 1][j][x - 1])
                if j > 0:
                    mn = min(mn, r[i][j - 1] + dp[i][j - 1][x - 1])
                if i < n - 1:
                    mn = min(mn, c[i][j] + dp[i + 1][j][x - 1])
                if j < m - 1:
                    mn = min(mn, r[i][j] + dp[i][j + 1][x - 1])
                dp[i][j][x] = mn
    for i in range(n):
        row_out = []
        for j in range(m):
            row_out.append(str(2 * dp[i][j][k // 2]))
        # print(" ".join(row_out))
        pass


def main(n):
    if n < 1:
        n = 1
    n_rows = n
    m_cols = n
    k_steps = 2 * (n if n % 2 == 0 else n + 1)
    r = []
    for i in range(n_rows):
        row = []
        for j in range(m_cols - 1):
            val = (i + 1) * (j + 2)
            row.append(val)
        r.append(row)
    c = []
    for i in range(n_rows - 1):
        row = []
        for j in range(m_cols):
            val = (i + j + 3)
            row.append(val)
        c.append(row)
    run_algorithm(n_rows, m_cols, k_steps, r, c)


if __name__ == "__main__":
    main(3)