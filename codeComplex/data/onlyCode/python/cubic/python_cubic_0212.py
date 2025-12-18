import os, sys
from io import BytesIO, IOBase
from math import log2, ceil, sqrt, gcd
from _collections import deque
import heapq as hp
from bisect import bisect_left, bisect_right

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
mod = 10 ** 9 + 7

R,G,B=map(int,input().split())
r=list(map(int,input().split()))
g=list(map(int,input().split()))
b=list(map(int,input().split()))
r.sort(reverse=True)
g.sort(reverse=True)
b.sort(reverse=True)
dp=[[[0]*(B+1) for _ in range(G+1)] for __ in range(R+1)]
ans=0
for i in range(R+1):
    for j in range(G+1):
        for k in range(B+1):
            if i>0 and j>0 and k>0:
                dp[i][j][k] = max(dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1],
                                  dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1],
                                  dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
            elif i>0 and j>0:
                dp[i][j][k] =dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
            elif i>0 and k>0:
                dp[i][j][k] = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                ans = max(ans, dp[i][j][k])
            elif j>0 and k>0:
                dp[i][j][k]=dp[i][j-1][k-1]+g[j-1]*b[k-1]
            ans=max(ans,dp[i][j][k])
# for i in dp:
#     print(i)
print(ans)




