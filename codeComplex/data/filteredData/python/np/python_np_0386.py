import os
import sys
from collections import defaultdict
from bisect import *
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

def ok(here, n, m, a):
    have = defaultdict(lambda: -1)
    for j in range(n):
        b = a[j]
        s = ''
        for i in b:
            if i >= here:
                s += '1'
            else:
                s += '0'
        have[int(s, 2)] = j

    full_mask = (1 << m) - 1
    # upper bound of 2**m-1 is at most 2**10-1=1023 since m<=10 in our generator
    for i in range(300):
        for j in range(300):
            if (i | j) == full_mask and have[i] != -1 and have[j] != -1:
                return (have[i] + 1, have[j] + 1)
    return -1

def main(n):
    # n controls matrix size; keep m small so 2**m is reasonable
    if n <= 0:
        print(-1)
        return
    m = 10
    # generate a deterministic n x m matrix
    a = []
    for i in range(n):
        row = [((i * m + j) % (2 * n + 5)) for j in range(m)]
        a.append(row)

    low = 0
    high = 10 ** 9
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2
        here = ok(mid, n, m, a)
        if here != -1:
            ans = here
            low = mid + 1
        else:
            high = mid - 1

    if ans == -1:
        print(-1)
    else:
        print(*ans)

if __name__ == "__main__":
    main(5)