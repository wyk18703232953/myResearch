#!/usr/bin/env python
import os
import sys
import time
from io import BytesIO, IOBase


def main():
    max_int = 10 ** 9
    d = ((1, 0), (-1, 0), (0, 1), (0, -1))
    n, m, k = li_input()
    H = []
    for i in range(n):
        H.append(li_input() + [max_int])

    V = []
    for i in range(n - 1):
        V.append(li_input())

    V.append([max_int] * m)

    if k % 2:
        for i in range(n):
            print(' '.join(['-1'] * m))
        return

    k //= 2

    DP0 = [[0] * (m + 1) for _ in range(n + 1)]
    DP1 = [[0] * (m + 1) for _ in range(n + 1)]

    for kk in range(k):
        for i in range(n):
            for j in range(m):
                l = DP0[i][j - 1] + H[i][j - 1]
                r = DP0[i][j + 1] + H[i][j]
                u = DP0[i - 1][j] + V[i - 1][j]
                d = DP0[i + 1][j] + V[i][j]
                DP1[i][j] = min(l, r, u, d)

        DP0, DP1 = DP1, DP0

    O = []
    for row in DP0[:-1]:
        O.append(' '.join((str(n * 2) for n in row[:-1])))

    print('\n'.join(O))


############

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


def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def i_input():
    return int(input())


def l_input():
    return input().split()


def li_input():
    return list(map(int, l_input()))


def il_input():
    return list(map(int, l_input()))


# endregion

if __name__ == "__main__":
    TT = time.time()
    main()
    # print("\n", time.time() - TT)
