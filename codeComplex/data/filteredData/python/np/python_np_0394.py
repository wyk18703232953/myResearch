import os
import sys
from io import BytesIO, IOBase

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
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2)
            self.buffer.write(b)
            self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0)
            self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdout = IOWrapper(sys.stdout)


def solve_with_matrix(A):
    n = len(A)
    if n == 0:
        return [-1, -1]
    m = len(A[0]) if A[0] else 0
    if m == 0:
        return [-1, -1]

    lo = 1 << 32
    hi = -1 << 32
    for i in range(n):
        row = A[i]
        if not row:
            continue
        rmin = row[0]
        rmax = row[0]
        for v in row:
            if v < rmin:
                rmin = v
            if v > rmax:
                rmax = v
        if rmin < lo:
            lo = rmin
        if rmax > hi:
            hi = rmax

    best = -1
    ans = [-1, -1]

    def possible(x):
        nonlocal best, ans
        M = [-1] * (1 << m)
        for i in range(n):
            mask = 0
            row = A[i]
            for j in range(m):
                if row[j] >= x:
                    mask |= 1 << j
            M[mask] = i
        full = (1 << m) - 1
        for m0 in range(1 << m):
            if M[m0] == -1:
                continue
            for m1 in range(1 << m):
                if M[m1] == -1:
                    continue
                if (m0 | m1) == full:
                    if best < x:
                        best = x
                        ans = [M[m0] + 1, M[m1] + 1]
                    return True
        return False

    possible(hi)
    possible(lo)

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if possible(mid):
            lo = mid
        else:
            hi = mid

    return ans


def main(n):
    if n <= 0:
        n = 1
    m = max(1, min(8, n))
    rows = n
    A = [[(i * m + j) % (n + m) for j in range(m)] for i in range(rows)]
    ans = solve_with_matrix(A)
    print(*ans)


if __name__ == "__main__":
    main(5)