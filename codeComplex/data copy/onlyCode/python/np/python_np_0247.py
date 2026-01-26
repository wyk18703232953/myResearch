import os
import sys
from io import BytesIO,IOBase

def main():
    n,m,k = map(int,input().split())
    a = list(map(float,input().split()))
    tree = [[0]*n for _ in range(n)]
    for i in range(k):
        x,y,z = map(int,input().split())
        tree[x-1][y-1] = float(z)
    po = [1]
    while len(po) != n:
        po.append(po[-1]*2)
    dp = [[0]*(po[-1]*2) for _ in range(n)]
    for i in range(n):
        dp[i][po[i]] = a[i]
    for i in range(po[-1]*2):
        for j in range(n):
            if i&po[j]:
                for k in range(n):
                    if not (i&po[k]):
                        dp[k][i+po[k]] = max(dp[k][i+po[k]],dp[j][i]+a[k]+tree[j][k])
    ma = 0
    for i in range(po[-1]*2):
        if bin(i)[2:].count("1") == m:
            for j in range(n):
                ma = max(ma,dp[j][i])
    print(int(ma))

# region fastio
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self,file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZE))
            self.newlines = b.count(b"\n")+(not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self,file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s:self.buffer.write(s.encode("ascii"))
        self.read = lambda:self.buffer.read().decode("ascii")
        self.readline = lambda:self.buffer.readline().decode("ascii")

sys.stdin,sys.stdout = IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input = lambda:sys.stdin.readline().rstrip("\r\n")

if __name__ == "__main__":
    main()