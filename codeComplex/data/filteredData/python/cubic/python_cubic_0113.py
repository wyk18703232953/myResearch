import os, sys
from io import BytesIO, IOBase
from math import inf, isinf

def solve(s, t):
    if len(t) == 1:
        if s.count(t[0]):
            return 'YES'
        return 'NO'
    for i in range(1, len(t)):
        dp = [[-inf] * (i + 1) for _ in range(len(s) + 1)]
        dp[0][0] = 0
        for j in range(len(s)):
            dp[j + 1] = dp[j][:]
            for k in range(i + 1):
                if k != i and s[j] == t[k]:
                    dp[j + 1][k + 1] = max(dp[j + 1][k + 1], dp[j][k])
                if dp[j][k] + i != len(t) and not isinf(dp[j][k]) and s[j] == t[dp[j][k] + i]:
                    dp[j + 1][k] = max(dp[j + 1][k], dp[j][k] + 1)
        for l in range(len(s) + 1):
            if dp[l][-1] == len(t) - i:
                return 'YES'
    return 'NO'

def generate_case(n, idx):
    # Deterministically generate (s, t) based on n and test index
    # Map n to lengths; keep them reasonable for experiments
    len_t = max(2, n // 3 + (idx % 3))
    len_s = max(len_t, n + idx)
    alphabet = "abcd"
    s = "".join(alphabet[(i + idx) % len(alphabet)] for i in range(len_s))
    t = "".join(alphabet[(i * 2 + idx) % len(alphabet)] for i in range(len_t))
    return s, t

def main(n):
    # n controls number of test cases and scale of strings
    t = max(1, n)
    results = []
    for i in range(t):
        s, tt = generate_case(n, i)
        results.append(solve(s, tt))
    for r in results:
        # print(r)
        pass

# Fast IO Region (left intact but unused for input)
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