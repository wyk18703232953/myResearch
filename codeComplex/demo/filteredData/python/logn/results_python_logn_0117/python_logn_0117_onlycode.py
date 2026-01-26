import os
import sys
from io import BytesIO, IOBase
import heapq as h 
from bisect import bisect_left

from types import GeneratorType
BUFSIZE = 8192
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        import os
        self.os = os
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = self.os.read(self._fd, max(self.os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            self.os.write(self._fd, self.buffer.getvalue())
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
 
import time
start_time = time.time()

import collections as col
import math, string
from functools import reduce

def getInts():
    return [int(s) for s in input().split()]

def getInt():
    return int(input())

def getStrs():
    return [s for s in input().split()]

def getStr():
    return input()

def listStr():
    return list(input())


"""
The max XOR comes from finding the longest *distinct* lengths
Within those sets, find the longest distinct lengths again
Etc

Suppose the max is 
10011110010111

And the min is
00000101011010

Then we have everything between

So the max would be
11111111111111

Fill the bits greedily
Can we fill bit one?
Can we fill bit two with that subset? Etc

Are L and R distinct lengths? If not, substract the largest bit from each
If so, add that bit to our answer, and subtract the largest bit from R
Repeat
"""


def solve():
    L, R = getInts()
    if L == R:
        return 0
    l = len(bin(L)[2:])
    r = len(bin(R)[2:])
    while l == r:
        L -= pow(2,r-1)
        R -= pow(2,r-1)
        l = len(bin(L)[2:])
        r = len(bin(R)[2:])
    return pow(2,r)-1

#for _ in range(getInt()):    
print(solve())
