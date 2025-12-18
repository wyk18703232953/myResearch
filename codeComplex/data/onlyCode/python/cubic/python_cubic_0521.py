import os, sys
from io import BytesIO, IOBase


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
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


class dict(dict):
    def __missing__(self, key):
        return 0


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda dtype: list(map(dtype, input().split()))
inp_2d = lambda dtype, n: [dtype(input()) for _ in range(n)]
inp_2ds = lambda dtype, n: [inp(dtype) for _ in range(n)]
inp_enu = lambda dtype: [(i, x) for i, x in enumerate(inp(dtype))]
inp_enus = lambda dtype, n: [[i] + [inp(dtype)] for i in range(n)]
ceil1 = lambda a, b: (a + b - 1) // b
valid = lambda x, y: -1 < x < n and -1 < y < m
dx, dy = (0, 1, 0, -1, 1, -1, 1, -1), (1, 0, -1, 0, 1, -1, -1, 1)

n, m, k = inp(int)
if k & 1:
    [print(*([-1] * m)) for _ in range(n)]
    exit()

right, down = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
mem = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]

for _ in range(n):
    for i, j in enumerate(inp(int)):
        right[_][i] = j

for _ in range(n - 1):
    for i, j in enumerate(inp(int)):
        down[_][i] = j

for i in range(n):
    for j in range(m):
        mem[i][j] = 0

for k1 in range(1, k // 2 + 1):
    mem0 = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            mem0[i][j] = min(mem[i - 1][j] + down[i - 1][j], mem[i + 1][j] + down[i][j],
                             mem[i][j - 1] + right[i][j - 1], mem[i][j + 1] + right[i][j])

    mem = mem0

[print(*[mem[i][x] * 2 for x in range(m)]) for i in range(n)]
