#------------------------template--------------------------#
import os
import sys
from math import *
from collections import *
# from fractions import *
# from heapq import*
from bisect import *
from io import BytesIO, IOBase
def vsInput():
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
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
ALPHA='abcdefghijklmnopqrstuvwxyz'
M=998244353
EPS=1e-6
def Ceil(a,b): return a//b+int(a%b>0)
def value():return tuple(map(int,input().split()))
def array():return [int(i) for i in input().split()]
def Int():return int(input())
def Str():return input()
def arrayS():return [i for i in input().split()]


#-------------------------code---------------------------#
# vsInput()


def ok(a,b,c):

    # print(a[0],b,c)

    n = a[0][-1]
    ans = []
    for i in range(a[0][0]): ans.append([a[1]]*n)

    l = n
    r = n - a[0][0]

    for i in range(2):
        for j in range(2):

            l1,r1 = b[0]
            l2,r2 = c[0]

            if(i): l1,r1 = r1,l1
            if(j): l2,r2 = r2,l2

            if(l1 == l):
                if(l2 != l or r1 + r2 != r): continue

                for k in range(r1): ans.append([b[1]]*n)
                for k in range(r2): ans.append([c[1]]*n)
                return ans


            if(l1 == r):
                if(l2 != r or r1 + r2 != l): continue

                for k in range(r): ans.append( [b[1]]*r1 + [c[1]]*r2)
                return ans

    return False


l1,r1,l2,r2,l3,r3 = value()

a = [sorted((l1,r1)),'A']
b = [sorted((l2,r2)),'B']
c = [sorted((l3,r3)),'C']

A = ok(a,b,c)
B = ok(b,a,c)
C = ok(c,a,b)

if(A):
    print(len(A))
    for i in A: print(*i,sep="")
elif(B): 
    print(len(B))
    for i in B: print(*i,sep="")
elif(C):
    print(len(C))
    for i in C: print(*i,sep="")
else: 
    print(-1)






















