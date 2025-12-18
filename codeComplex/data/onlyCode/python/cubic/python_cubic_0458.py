import os
import sys
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
#######################################
from heapq import heapify,heappush as hp,heappop as hpop
def check(x,y):
    if 0<=x<=n-1 and 0<=y<=m-1:
        return True
    return False
n,m,k=map(int,input().split())
l1=[]
l2=[]
for i in range(n):
    l1.append(list(map(int,input().split())))
for  i in range(n-1):
    l2.append(list(map(int,input().split())))
inf=10**18
dp=[[[inf]*21 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        if check(i,j+1):
            dp[i][j][1]=min(l1[i][j],dp[i][j][1])
        if check(i,j-1):
            dp[i][j][1]=min(l1[i][j-1],dp[i][j][1])
        if check(i+1,j):
            dp[i][j][1]=min(l2[i][j],dp[i][j][1])
        if check(i-1,j):
            dp[i][j][1]=min(l2[i-1][j],dp[i][j][1])
for x in range(2,k//2+1):
    for i in range(n):
        for j in range(m):
            if check(i,j+1):
                dp[i][j][x]=min(l1[i][j]+dp[i][j+1][x-1],dp[i][j][x])
            if check(i,j-1):
                dp[i][j][x]=min(l1[i][j-1]+dp[i][j-1][x-1],dp[i][j][x])
            if check(i+1,j):
                dp[i][j][x]=min(l2[i][j]+dp[i+1][j][x-1],dp[i][j][x])
            if check(i-1,j):
                dp[i][j][x]=min(l2[i-1][j]+dp[i-1][j][x-1],dp[i][j][x])
           
ans=[[inf]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if k%2:
            ans[i][j]=-1
            continue
        ans[i][j]=2*dp[i][j][k//2] 
for i in ans:
    print(*i)
