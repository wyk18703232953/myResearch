import os
import sys
from io import BytesIO, IOBase
from array import array

def core_algorithm(n, M):
    comb = [[0] * (n + 1) for _ in range(n + 1)]
    comb[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i + 1):
            comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % M

    dp = [array('i', [0] * (n + 1)) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][0] = pow(2, i - 1, M)
    for j in range(1, n + 1):
        for i in range(3, n + 1):
            for x in range(1, i - 1):
                dp[i][j] = (dp[i][j] + dp[i - 1 - x][j - 1] * dp[x][0] * comb[i - j][x]) % M
    su = 0
    for i in range(n + 1):
        su = (su + dp[n][i]) % M
    return su

def main(n):
    if n < 1:
        n = 1
    M = 10**9 + 7
    result = core_algorithm(n, M)
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
    main(10)