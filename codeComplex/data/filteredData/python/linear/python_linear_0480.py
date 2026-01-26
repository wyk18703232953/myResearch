import sys
import os
import io
import datetime
import math
import functools
import itertools
import operator
import bisect
import fractions
import statistics
from collections import deque, defaultdict, OrderedDict, Counter
from fractions import Fraction
from decimal import Decimal
from heapq import heappush, heappop, heapify, _heapify_max, _heappop_max, nsmallest, nlargest

def intersection(l1, r1, l2, r2):
    if l1 > r2 or r1 < l2:
        return [0, 0]

    else:
        return [max(l1, l2), min(r1, r2)]

def core_logic(z):
    n = len(z)
    if n == 0:
        return 0
    pref = []
    suff = []

    pix, piy = intersection(z[0][0], z[0][1], z[0][0], z[0][1])
    six, siy = intersection(z[-1][0], z[-1][1], z[-1][0], z[-1][1])

    for i in range(n):
        pix, piy = intersection(pix, piy, z[i][0], z[i][1])
        pref.append([pix, piy])

    for i in range(n - 1, -1, -1):
        six, siy = intersection(six, siy, z[i][0], z[i][1])
        suff.append([six, siy])

    suff = suff[::-1]

    if n == 1:
        return 0

    ans = max(suff[1][1] - suff[1][0], pref[n - 2][1] - pref[n - 2][0])
    for i in range(1, n - 1):
        inter = intersection(pref[i - 1][0], pref[i - 1][1], suff[i + 1][0], suff[i + 1][1])
        ans = max(ans, inter[1] - inter[0])
    return ans

def generate_data(n):
    if n <= 0:
        return []
    # Deterministic interval generation:
    # z[i] = [i, 2*i + (i % 3)]
    # Ensures intervals are simple and scale linearly with n
    z = [[i, 2 * i + (i % 3)] for i in range(n)]
    return z

def main(n):
    starttime = datetime.datetime.now()
    z = generate_data(n)
    ans = core_logic(z)
    sys.stdout.write(str(ans) + "\n")
    endtime = datetime.datetime.now()
    time = (endtime - starttime).total_seconds() * 1000
    sys.stdout.write("Time: " + str(time) + " ms\n")

class FastReader(io.IOBase):
    newlines = 0

    def __init__(self, fd, chunk_size=1024 * 8):
        self._fd = fd
        self._chunk_size = chunk_size
        self.buffer = io.BytesIO()

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self, size=-1):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self._chunk_size if size == -1 else size))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

class FastWriter(io.IOBase):

    def __init__(self, fd):
        self._fd = fd
        self.buffer = io.BytesIO()
        self.write = self.buffer.write

    def flush(self):
        os.write(self._fd, self.buffer.getvalue())
        self.buffer.truncate(0), self.buffer.seek(0)

class FastStdin(io.IOBase):
    def __init__(self, fd=0):
        self.buffer = FastReader(fd)
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

class FastStdout(io.IOBase):
    def __init__(self, fd=1):
        self.buffer = FastWriter(fd)
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.flush = self.buffer.flush

if __name__ == "__main__":
    sys.stdin = FastStdin()
    sys.stdout = FastStdout()
    main(10)