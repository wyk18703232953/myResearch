import os
import sys
from io import BytesIO, IOBase
from collections import Counter,defaultdict
from heapq import heappush, heappop
nmbr = lambda: int(input())
lst = lambda: list(map(int, input().split()))
def main():
    for _ in range(1):  # nmbr()):
        n = nmbr()
        d = defaultdict(int)
        for i in range(n):
            u, v = lst()
            d[u] += 1
            d[v + 1] -= 1
        ks = sorted(d.keys())
        ks_n = len(ks)
        for i in range(1, ks_n):
            d[ks[i]] += d[ks[i - 1]]
        l = Counter()
        for i in range(ks_n - 1):
            times = d[ks[i]]
            cnt = ks[i + 1] - ks[i]
            l[times] += cnt
        for i in range(1, n + 1):
            sys.stdout.write(str(l[i]) + ' ')

        # sys.stdout.write(str(ans)+'\n')
    # sys.stdout.flush()

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
input = lambda: sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    for t in range(1):main()#int(input())):