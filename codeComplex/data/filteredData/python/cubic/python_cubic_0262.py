import os
import heapq
import sys, threading
import math
import bisect
import operator
from collections import defaultdict
from io import BytesIO, IOBase

sys.setrecursionlimit(10 ** 7)

def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a % b)

def power(x, p, m):
    res = 1
    while p:
        if p & 1:
            res = (res * x) % m
        x = (x * x) % m
        p >>= 1
    return res

def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

rr = 0
gg = 0
bb = 0
dp = []

def func(x, y, z, red, green, blue):
    if (x >= rr and y >= gg) or (y >= gg and z >= bb) or (x >= rr and z >= bb):
        return 0
    if dp[x][y][z] != -1:
        return dp[x][y][z]
    take = 0
    if x < rr and y < gg:
        take = max(take, red[x] * green[y] + func(x + 1, y + 1, z, red, green, blue))
    if y < gg and z < bb:
        take = max(take, green[y] * blue[z] + func(x, y + 1, z + 1, red, green, blue))
    if x < rr and z < bb:
        take = max(take, red[x] * blue[z] + func(x + 1, y, z + 1, red, green, blue))
    dp[x][y][z] = take
    return take

def generate_arrays_from_n(n):
    # Map n to sizes of the three arrays in a deterministic way.
    # Ensure each is at least 1.
    r = max(1, n // 3)
    g = max(1, n // 3 + (1 if n % 3 > 0 else 0))
    b = max(1, n - r - g)
    # Deterministic content using simple arithmetic patterns.
    red = [(i * 2 + 1) for i in range(r)]
    green = [(i * 3 + 2) for i in range(g)]
    blue = [(i * 5 + 3) for i in range(b)]
    return r, g, b, red, green, blue

def main(n):
    global rr, gg, bb, dp
    rr, gg, bb, red, green, blue = generate_arrays_from_n(n)
    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)
    max_size = max(rr, gg, bb) + 1
    dp.clear()
    for i in range(max_size):
        temp = []
        for j in range(max_size):
            lis = [-1] * max_size
            temp.append(lis)
        dp.append(temp)
    result = func(0, 0, 0, red, green, blue)
    # print(result)
    pass

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

if __name__ == "__main__":
    main(60)