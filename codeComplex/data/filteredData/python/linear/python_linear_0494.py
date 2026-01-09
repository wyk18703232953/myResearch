import sys
import math
from io import BytesIO, IOBase
from fractions import Fraction
import collections
from itertools import permutations
from collections import defaultdict
from collections import deque
import threading

BUFSIZE = 8192

class SegmentTree:
    def __init__(self, data, default=-10**6, func=lambda a, b: max(a,b)):
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
    def __init__(self, data, default=10**6, func=lambda a, b: min(a,b)):
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

MOD=10**9+7
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

mod=10**9+7
omod=998244353

prime = [True for _ in range(200001)]
pp=[0]*200001
def SieveOfEratosthenes(n=200000):
    p = 2
    while (p * p <= n):
        if prime[p] == True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

def core_algorithm(a):
    n = len(a)
    if n == 0:
        return []
    if n == 1:
        return [1]
    dp=[[-1 for _ in range(5)] for _ in range(n)]
    for i in range(1, min(2, n)):
        if a[i] < a[i-1]:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k > j:
                        ch = k
                dp[i][j] = ch
        elif a[i] > a[i-1]:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k < j:
                        ch = k
                dp[i][j] = ch

        else:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k != j:
                        ch = k
                dp[i][j] = ch
    for i in range(2, n):
        if a[i] < a[i-1]:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k > j and dp[i-1][k] != -1:
                        ch = k
                dp[i][j] = ch
        elif a[i] > a[i-1]:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k < j and dp[i-1][k] != -1:
                        ch = k
                dp[i][j] = ch

        else:
            for j in range(5):
                ch=-1
                for k in range(5):
                    if k != j and dp[i-1][k] != -1:
                        ch = k
                dp[i][j] = ch
    ind=-1
    for i in range(5):
        if dp[-1][i] != -1:
            ind = i
    if ind == -1:
        return [-1]
    res=[ind+1]
    for i in range(n-1, 0, -1):
        res.append(dp[i][ind] + 1)
        ind = dp[i][ind]
    return res[::-1]

def generate_input(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    a = [0]*n
    a[0] = 0
    for i in range(1, n):
        if i % 3 == 1:
            a[i] = a[i-1] + 1
        elif i % 3 == 2:
            a[i] = a[i-1] - 1

        else:
            a[i] = a[i-1]
    return a

def main(n):
    a = generate_input(n)
    res = core_algorithm(a)
    # print(len(a))
    pass
    # print(" ".join(str(x) for x in a))
    pass
    # print(" ".join(str(x) for x in res))
    pass
if __name__ == "__main__":
    main(10)