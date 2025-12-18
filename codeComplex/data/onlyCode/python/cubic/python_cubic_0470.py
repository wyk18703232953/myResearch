import os, sys
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


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
n,m,k=map(int,input().split())
row=[]
for _ in range(n):
    row.append([10**6+2]+list(map(int,input().split()))+[10**6+2])
col=[[10**6+2]*(m+2)]
for _ in range(n-1):
    col.append([10**6+2]+list(map(int,input().split()))+[10**6+2])
col.append([10**6+2]*(m+2))
if  k%2:
    dp=[[-1 for i in range(m)] for j in range(n)]
else:
    k=k//2
    dp = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            dp[i][j]=2*min(row[i][j],row[i][j+1],col[i][j+1],col[i+1][j+1])
    k-=1
    while k:
       # print(row,col)
        k-=1
        temp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                ck=dp[i][j]*8
                if i>=1:
                    ck=min(ck,dp[i-1][j]+2*col[i][j+1])
                if i<n-1:
                    ck=min(ck,dp[i+1][j]+2*col[i+1][j+1])
                if j>=1:
                    ck=min(ck,dp[i][j-1]+2*row[i][j])
                if j<m-1:
                    ck=min(ck,dp[i][j+1]+2*row[i][j+1])
                temp[i][j]=ck


        dp=temp

for i in dp:
    print(*i)
