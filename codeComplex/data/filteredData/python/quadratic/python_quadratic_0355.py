import math
from io import BytesIO, IOBase
from fractions import Fraction
import collections
from itertools import permutations
from collections import defaultdict
from collections import deque
import threading

BUFSIZE = 8192
 
class FastIO(IOBase):
    newlines = 0
    
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
     
    def read(self):
        return self.buffer.read()
 
    def readline(self):
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.buffer.truncate(0), self.buffer.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

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
        self.factorials += nextArr>
        return self.factorials[n]
 
    def inv(self, n):
        if n <= -1:
            raise ValueError("n must be non-negative")
        p = self.MOD
        pi = n % p
        if pi < len(self.invModulos):
            return self.invModulos[pi]
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

prime = [True for _ in range(10)] 
pp = [0]*10

def SieveOfEratosthenes(n=10):
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p, n+1, p):
                pp[i] += 1
                prime[i] = False
        p += 1

def binarySearch(arr, n, key):
    left = 0
    right = n-1
    res = arr[n-1]
    while left <= right:
        mid = (right + left)//2
        if arr[mid] >= key:
            res = arr[mid]
            right = mid-1

        else:
            left = mid + 1
    return res

def binarySearch1(arr, n, key):
    left = 0
    right = n-1
    res = arr[0]
    while left <= right:
        mid = (right + left)//2
        if arr[mid] > key:
            right = mid-1

        else:
            res = arr[mid]
            left = mid + 1
    return res

def solve_grid(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    l = grid
    tot = []
    done = [[0 for _ in range(m)] for _ in range(n)]
    colsum = [[0 for _ in range(m)] for _ in range(n)]
    rowsum = [[0 for _ in range(m)] for _ in range(n)]
    col = [[0 for _ in range(m)] for _ in range(n)]
    row = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                rowsum[i][j] = 1
                colsum[i][j] = 1
                row[i][j] = 1
                col[i][j] = 1
    for i in range(n):
        for j in range(1, m):
            if l[i][j] == '.':
                continue
            rowsum[i][j] += rowsum[i][j-1]
    for i in range(n):
        for j in range(m-2, -1, -1):
            if l[i][j] == '.':
                continue
            row[i][j] += row[i][j+1]
    for i in range(m):
        for j in range(n-2, -1, -1):
            if l[j][i] == '.':
                continue
            col[j][i] += col[j+1][i]
    for i in range(m):
        for j in range(1, n):
            if l[j][i] == '.':
                continue
            colsum[j][i] += colsum[j-1][i]
    def check(x, y):
        i = x
        j = y
        ans = min(row[i][j], rowsum[i][j], colsum[i][j], col[i][j]) - 1
        if ans == 0:
            return []
        return [ans]
    h = [[0 for _ in range(m+1)] for _ in range(n)]
    v = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                ans = check(i, j)
                for j1 in ans:
                    tot.append([i+1, j+1, j1])
                    h[i][j-j1] += 1
                    h[i][j+j1+1] -= 1
                    v[i-j1][j] += 1
                    v[i+j1+1][j] -= 1
    for i in range(n):
        for j in range(1, m):
            h[i][j] += h[i][j-1]
    for i in range(m):
        for j in range(1, n):
            v[j][i] += v[j-1][i]
    for i in range(n):
        for j in range(m):
            if l[i][j] == '*' and h[i][j] == 0 and v[i][j] == 0:
                return -1, []
    return len(tot), tot

def generate_grid(n):
    if n <= 0:
        return []
    rows = n
    cols = n
    grid = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 2 == 0:
                row_chars.append('*')

            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))
    return grid

def main(n):
    grid = generate_grid(n)
    count, stars = solve_grid(grid)
    # print(count)
    pass
    for triple in stars:
        # print(*triple)
        pass
if __name__ == "__main__":
    main(5)