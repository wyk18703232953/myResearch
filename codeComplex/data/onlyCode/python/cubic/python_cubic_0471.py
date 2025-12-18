#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import threading 
from bisect import bisect_right
from math import gcd,log
from collections import Counter,defaultdict,deque
from pprint import pprint
from itertools import permutations 
from bisect import bisect_right
from random import randint as rti 
# import deque
n,m=0,0


    



def main(tnum):
    global n,m,d
    n,m,k=map(int,input().split())
    if k%2:
        ans=[[-1]*m for i in range(n)]
        for li in ans:
            print(*li)
        return 
    cost=dict()
    dp=[[float('inf')]*m for i in range(n)] 
    crr=[]
    rrr=[]
    for i in range(n):
        arr=list(map(int,input().split()))
        for j in range(m-1):
            dp[i][j]=min(dp[i][j],arr[j])
            dp[i][j+1]=min(dp[i][j+1],arr[j])
        crr.append(arr)


    for i in range(n-1):
        arr=list(map(int,input().split())) 
        for j in range(m):
            dp[i][j]=min(dp[i][j],arr[j])
            dp[i+1][j]=min(dp[i+1][j],arr[j])


        rrr.append(arr)

    for i in range(1,k//2):
        ndp=[[float('inf')]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                x,y=i,j
                if x>0:
                    ndp[i][j]=min(ndp[i][j],dp[x-1][y]+rrr[x-1][y])
                if x<n-1:
                    ndp[i][j]=min(ndp[i][j],dp[x+1][y]+rrr[x][y])
                if y>0:
                    ndp[i][j]=min(ndp[i][j],dp[x][y-1]+crr[x][y-1])
                if y<m-1:
                    ndp[i][j]=min(ndp[i][j],dp[x][y+1]+crr[x][y])
        dp=ndp
    for li in dp:
        li=[2*x for x in li]
        print(*li)  















    


        




    

    








        
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
 
# endregion
 
if __name__ == "__main__":

    for _ in range(1): 
        main(_+1)



