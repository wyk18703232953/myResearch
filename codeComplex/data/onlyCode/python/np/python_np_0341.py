# by the authority of GOD     author: manhar singh sachdev #

import os,sys
from io import BytesIO,IOBase

def main():
    mod = 10**9+7
    n,T = map(int,input().split())
    y = 1<<n
    dp = [[0]*3 for _ in range(y)]
    # already taken ; genre
    peo = [list(map(int,input().split())) for _ in range(n)]
    # duration ; genre
    for ind,i in enumerate(peo):
        peo[ind][1] -= 1
        dp[1<<ind][i[1]] = 1
    for i in range(y):
        for j in range(3):
            if not dp[i][j]:
                continue
            mask = 1
            for k in range(n):
                if i&mask or peo[k][1] == j:
                    mask <<= 1
                    continue
                dp[i|mask][peo[k][1]] = (dp[i|mask][peo[k][1]]+dp[i][j])%mod
                mask <<= 1
    ans = 0
    for i in range(y):
        ans1,mask = 0,1
        for j in range(n):
            if i&mask:
                ans1 += peo[j][0]
            mask <<= 1
        if ans1 == T:
            ans = (ans+sum(dp[i]))%mod
    print(ans)

#Fast IO Region
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

if __name__ == '__main__':
    main()