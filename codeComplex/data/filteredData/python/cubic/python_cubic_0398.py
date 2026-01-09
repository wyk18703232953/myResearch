from io import BytesIO, IOBase
import sys
import math
import os
from collections import defaultdict
from math import ceil
from bisect import bisect_left, bisect_left


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


def solve(n, m, k, horizontal, vertical):
    if k % 2 or max(n, m) == 1:
        for _ in range(n):
            # print(*[-1] * m)
            pass
        return
    dp = [[[0] * (k // 2 + 1) for _ in range(m)] for _ in range(n)]
    for length in range(1, k // 2 + 1):
        for i in range(n):
            for j in range(m):
                left_path = math.inf if j == 0 else horizontal[i][j - 1] + dp[i][j - 1][length - 1]
                right_path = math.inf if j == m - 1 else horizontal[i][j] + dp[i][j + 1][length - 1]
                top_path = math.inf if i == 0 else vertical[i - 1][j] + dp[i - 1][j][length - 1]
                bottom_path = math.inf if i == n - 1 else vertical[i][j] + dp[i + 1][j][length - 1]
                dp[i][j][length] = min(left_path, right_path, top_path, bottom_path)
    for i in range(n):
        for j in range(m):
            # print(dp[i][j][k // 2] * 2, end=" ")
            pass
        # print()
        pass


def main(n):
    # Interpret n as grid size; keep k small and even relative to n for scalability.
    if n < 2:
        rows = 1
        cols = 1
        k = 2

    else:
        rows = n
        cols = n
        # path length parameter, even, grows slowly with n
        k = 2 * (1 + n // 5)
    # Construct deterministic weights using simple arithmetic on indices
    horizontal = [[(i + j) % 7 + 1 for j in range(cols - 1)] for i in range(rows)]
    vertical = [[(i * 2 + j) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]
    solve(rows, cols, k, horizontal, vertical)


if __name__ == "__main__":
    main(5)