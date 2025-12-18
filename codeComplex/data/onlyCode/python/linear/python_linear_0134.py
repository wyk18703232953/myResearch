# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO, IOBase

def bit_count(x):
    ans = 0
    while x:
        x &= x-1
        ans += 1
    return ans

def main():
    n = input().strip()
    x = len(n)
    k = int(input())
    if n == '1':
        print(int(k==0))
        exit()
    if not k:
        print(1)
        exit()
    mod = 10**9+7
    dp = [0]*(x+1)
    dp[1] = 1
    for i in range(2,x+1):
        dp[i] = dp[bit_count(i)]+1
    dp1 = [[0]*(x+1) for _ in range(x+1)]
    # length ; set bits
    for i in range(x+1):
        dp1[i][0] = 1
    for i in range(1,x+1):
        for j in range(1,i+1):
            dp1[i][j] = (dp1[i-1][j-1]+dp1[i-1][j])%mod
    ans = 0
    cou = n.count('1')
    for i in range(1,x+1):
        if dp[i] != k:
            continue
        se = i
        for j in range(x):
            if n[j] == '0':
                continue
            ans = (ans+dp1[x-1-j][se]-(se==1 and k==1))%mod
            se -= 1
            if se < 0:
                break
        if cou == i:
            ans = (ans+1)%mod
    print(ans)

# Fast IO Region
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
    main()