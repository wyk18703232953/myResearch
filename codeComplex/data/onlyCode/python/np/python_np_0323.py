#Code by Sounak, IIESTS
#------------------------------warmup----------------------------

import os
import sys
import math
from io import BytesIO, IOBase
from fractions import Fraction
from collections import defaultdict
from itertools import permutations
 

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
 
#-------------------game starts now-----------------------------------------------------
n,k=map(int,sys.stdin.readline().split())
 
mod=998244353
dp=[[0,0,0,0] for x in range(k+3)]
dp[1][0]=1
dp[1][1]=1
dp[2][2]=1
dp[2][3]=1
newdp=[[0,0,0,0] for x in range(k+3)]
for i in range(n-1):
    
    for j in range(k+1):
        newdp[j+1][1]+=dp[j][0]
        newdp[j+1][3]+=dp[j][0]
        newdp[j+1][2]+=dp[j][0]
        newdp[j][0]+=dp[j][0]
        newdp[j][1]+=dp[j][1]
        newdp[j+1][3]+=dp[j][1]
        newdp[j+1][2]+=dp[j][1]
        newdp[j+1][0]+=dp[j][1]
        newdp[j][1]+=dp[j][2]
        newdp[j+2][3]+=dp[j][2]
        newdp[j][2]+=dp[j][2]
        newdp[j][0]+=dp[j][2]
        newdp[j][1]+=dp[j][3]
        newdp[j][3]+=dp[j][3]
        newdp[j+2][2]+=dp[j][3]
        newdp[j][0]+=dp[j][3]
        
        for a in range(3):
            for b in range(4):
                newdp[a+j][b]%=mod
    for a in range(k+3):
        for b in range(4):
            dp[a][b]=newdp[a][b]
            newdp[a][b]=0
ans=sum(dp[k])
ans%=mod
print(ans)