# template begins
#####################################
from io import BytesIO, IOBase
import sys
import math
import os
from collections import defaultdict
from math import ceil
from bisect import bisect_left, bisect_left


# region fastio

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
def input(): return sys.stdin.readline().rstrip("\r\n")
def mint(): return map(int, input().split())
def mfloat(): return map(float, input().split())


#####################################
# template ends
# Use the recursion snippet if heavy recursion is needed (depth>1000)
def solve():
    n, m, k = mint()
    horizontal = [list(mint()) for i in range(n)]
    vertical = [list(mint()) for i in range(n-1)]
    if k%2 or max(n, m)==1:
        for i in range(n):
            print(*[-1]*m)
        return
    """
    does it make sense to double back on a path if k is large enough?
    or are there cases when you need to make a loop?

    proof:
    if you have a path of length k that does not visit any edge more than once,
    we can split it into 2 paths of length k/2
    if one of them was cheaper than the other, we should have just back tracked on that
    hence, both must be the same
    in that case, you can just double any one

    should ideally double back on the same path if k is big enough
    just find the cheapest path of length k/2 and double it?

    how do you find the cheapest path of length k/2?

    dp?
    store the cheapest path of length x from every node,
    where x will be from 1 to k/2
    yeah should work
    dp[i][j][x] represents the cheapest path of length from g[i][j] of length x
    """
    dp = [[[0]*(k//2+1) for i in range(m)] for j in range(n)]
    for length in range(1, k//2+1):
        for i in range(n):
            for j in range(m):
                """
                we want cost_to_neighbour + dp[neigbour][length-1] to be min
                """
                left_path = math.inf if j==0 else horizontal[i][j-1]+dp[i][j-1][length-1]
                right_path = math.inf if j==m-1 else horizontal[i][j]+dp[i][j+1][length-1]
                top_path = math.inf if i==0 else vertical[i-1][j]+dp[i-1][j][length-1]
                bottom_path = math.inf if i==n-1 else vertical[i][j]+dp[i+1][j][length-1]
                dp[i][j][length] = min([left_path, right_path, top_path, bottom_path])
    for i in range(n):
        for j in range(m):
            print(dp[i][j][k//2]*2, end=' ')
        print()

    

def main():
    # t = int(input())
    t = 1
    for _ in range(t):
        solve()


if __name__ == "__main__":
    main()
