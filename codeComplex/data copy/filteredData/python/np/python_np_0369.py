import os
import sys
from io import BytesIO, IOBase
from math import factorial
from collections import Counter, defaultdict, deque
from heapq import heapify, heappop, heappush

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


mod = 998244353
INF = float('inf')

def comb(n, m):
    return factorial(n) / (factorial(m) * factorial(n - m)) if n >= m else 0

def perm(n, m):
    return factorial(n) // (factorial(n - m)) if n >= m else 0

def mdis(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def run_logic(n, m, arr):
    larr = [list(i) for i in zip(*arr)]
    larr.sort(key=lambda a: max(a), reverse=1)
    larr = larr[:n]

    res = 0

    def dfs(lst, pos=0):
        nonlocal res
        if pos == min(n, len(larr)):
            res = max(res, sum(lst))
            return
        for i in range(n):
            now = larr[pos][i:n] + larr[pos][0:i]
            nex = [max(now[j], lst[j]) for j in range(n)]
            dfs(nex, pos + 1)

    dfs([0] * n)
    return res


def main(n):
    T = n
    outputs = []
    for t in range(T):
        size = max(1, n)
        rows = size
        cols = size
        arr = [[(i * cols + j + t) % 1000 for j in range(cols)] for i in range(rows)]
        res = run_logic(rows, cols, arr)
        outputs.append(str(res))
    sys_stdout = IOWrapper(sys.stdout)
    for line in outputs:
        sys_stdout.write(line + "\n")
    sys_stdout.flush()


if __name__ == "__main__":
    main(3)