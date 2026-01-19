import math
from collections import defaultdict

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
    res = arr[n - 1]
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] >= key:
            res = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    return res

def binarySearch1(arr, n, key):
    left = 0
    right = n - 1
    res = arr[0]
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > key:
            right = mid - 1
        else:
            res = arr[mid]
            left = mid + 1
    return res

def solve_instance(l, n, m):
    pm = (1 << m) - 1
    def find(x):
        s = set()
        d = defaultdict(int)
        for i in range(n):
            a_bits = []
            row = l[i]
            for j in range(m):
                if row[j] >= x:
                    a_bits.append('1')
                else:
                    a_bits.append('0')
            a = int(''.join(a_bits), 2)
            d[a] = i
            s.add(a)
        s_list = list(s)
        len_s = len(s_list)
        for i in range(len_s):
            si = s_list[i]
            for j in range(i, len_s):
                sj = s_list[j]
                if (si | sj) == pm:
                    return [d[si] + 1, d[sj] + 1]
        return [-1, -1]
    st = 0
    end = 10**9
    ans = (0, 0)
    while st <= end:
        mid = (st + end) // 2
        res = find(mid)
        if res[0] != -1:
            ans = (res[0], res[1])
            st = mid + 1
        else:
            end = mid - 1
    return ans

def generate_data(n):
    if n < 1:
        n = 1
    m = max(1, n.bit_length())
    matrix = [[(i * m + j) % 1000 for j in range(m)] for i in range(n)]
    return matrix, n, m

def main(n):
    l, rows, cols = generate_data(n)
    ans = solve_instance(l, rows, cols)
    print(ans[0], ans[1])

if __name__ == "__main__":
    main(10)