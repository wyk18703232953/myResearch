import os
import heapq
import sys, threading
import math
import bisect
import operator
from collections import defaultdict

sys.setrecursionlimit(10 ** 5)
from io import BytesIO, IOBase


def gcd(a, b):
    if b == 0:

        return a
    else:
        return gcd(b, a % b)


def power(x, p, m):
    res = 1
    while p:
        if p & 1:
            res = (res * x) % m
        x = (x * x) % m
        p >>= 1
    return res


def inar():
    return [int(k) for k in input().split()]


def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)
rr=0
gg=0
bb=0
dp=[]
def func(x,y,z,red,green,blue):
    if (x>=rr and y>=gg) or (y>=gg and z>=bb) or (x>=rr and z>=bb):
        return 0
    if dp[x][y][z]!=-1:
        return dp[x][y][z]
    take=0
    if x<rr and y<gg:
        take=max(take,red[x]*green[y]+func(x+1,y+1,z,red,green,blue))
    if y<gg and z<bb:
        take=max(take,green[y]*blue[z]+func(x,y+1,z+1,red,green,blue))
    if x<rr and z<bb:
        take=max(take,red[x]*blue[z]+func(x+1,y,z+1,red,green,blue))
    dp[x][y][z]=take
    return take

def main():
    global rr,gg,bb,dp
    # t=int(input())
    for i in range(202):
        temp=[]
        for j in range(202):
            lis=[]
            for k in range(202):
                lis.append(-1)
            temp.append(lis)
        dp.append(temp)
    rr, gg, bb = map(int, input().split())
    red = inar()
    green = inar()
    blue = inar()
    red.sort(reverse=True)
    green.sort(reverse=True)
    blue.sort(reverse=True)
    print(func(0,0,0,red,green,blue))




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
    # threadin.Thread(target=main).start()
