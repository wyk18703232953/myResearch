import os
import sys
from io import BytesIO, IOBase


def check(mid: int, n: int, m: int, a, ans_holder) -> bool:
    dic = {}
    for i in range(n):
        bit = 0
        for j in range(m):
            if a[i][j] >= mid:
                bit += 1
            bit <<= 1
        dic[bit >> 1] = i
    full = (1 << m) - 1
    for x, idx in dic.items():
        for y, idy in dic.items():
            if x | y == full:
                ans_holder[0] = (idx + 1, idy + 1)
                return True
    return False


def solve(n: int):
    # interpret n as number of rows; fix m as a small constant
    m = 5
    if n <= 0:
        print(-1, -1)
        return
    # deterministic matrix generation
    a = [[(i * m + j) % 100 for j in range(m)] for i in range(n)]
    ans_holder = [(-1, -1)]
    le = 0
    ri = int(1e9)
    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid, n, m, a, ans_holder):
            le = mid + 1
        else:
            ri = mid - 1
    x, y = ans_holder[0]
    print(x, y)


def main(n: int):
    solve(n)


# region fastio (kept for structure, not used for input)

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


# endregion

if __name__ == "__main__":
    # example call; can be adjusted for experiments
    main(10)