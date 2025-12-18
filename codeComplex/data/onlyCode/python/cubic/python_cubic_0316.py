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
##########################################################
from collections import Counter
# c=sorted((i,int(val))for i,val in enumerate(input().split()))
import heapq
# c=sorted((i,int(val))for i,val in enumerate(input().split()))
# n = int(input())
# ls = list(map(int, input().split()))
# n, k = map(int, input().split())
# n =int(input())
#arr=[(i,x) for i,x in enum]
#arr.sort(key=lambda x:x[0])
#print(arr)
# e=list(map(int, input().split()))
from collections import Counter
#print("\n".join(ls))
#print(os.path.commonprefix(ls[0:2]))
#n=int(input())
from bisect import  bisect_right
#for _ in range(int(input())):
#n=int(input())
#arr = list(map(int, input().split()))
#for _ in range(int(input())):
#n, k = map(int, input().split())
import bisect
#n=int(input())
#n, p,q,r = map(int, input().split())
#arr = list(map(int, input().split()))
#n=int(input())
#nm,k = map(int, input().split())
#for _ in range(int(input())):
def find(x,y,z):
    if dp[x][y][z]!=-1:
        return dp[x][y][z]
    ans=0
    if x<r and y<g:
        ans=max(ans,rl[x]*gl[y]+find(x+1,y+1,z))
    if x<r and z<b:
        ans=max(ans,rl[x]*bl[z]+find(x+1,y,z+1))
    if y<g and z<b:
        ans=max(ans,gl[y]*bl[z]+find(x,y+1,z+1))

    dp[x][y][z]=ans
    return ans
r,g,b = map(int, input().split())
rl=sorted(list(map(int, input().split())),reverse=True)
gl=sorted(list(map(int, input().split())),reverse=True)
bl=sorted(list(map(int, input().split())),reverse=True)
dp=[[[-1]*(b+1) for i in range(g+1)]for i in range(r+1)]
print(find(0,0,0))

