import os,sys
from io import BytesIO, IOBase

from collections import deque, Counter,defaultdict as dft
from heapq import heappop ,heappush
from math import log,sqrt,factorial,cos,tan,sin,radians,log2,ceil,floor
from bisect import bisect,bisect_left,bisect_right
from decimal import *
import sys,threading
from itertools import permutations, combinations
from copy import deepcopy
input = sys.stdin.readline


ii = lambda: int(input())
si = lambda: input().rstrip()
mp = lambda: map(int, input().split())
ms=  lambda: map(str,input().strip().split(" "))
ml = lambda: list(mp())
mf = lambda: map(float, input().split())


alphs = "abcdefghijklmnopqrstuvwxyz"




def solve():
    


    def seq(nd,i):
        case=0
        vis[nd]=1
        for lnk in d[nd]:
            
            if not vis[lnk]:
                i,case=seq(lnk,i)
                if case:return i,case
            else:
                if lnk not in seen:
                    #print(seen,lnk)
                    case=1
                    break
                
        
        order[i]=nd
        seen.add(nd)
        
        return i-1,case
        
        
        
    
    def chk(word,dct,i):
        if i==k:
            res.append(dct['#'])
        else:
            if word[i] in dct:
                chk(word,dct[word[i]],i+1)
            if '_' in dct:
                chk(word,dct['_'],i+1)
    
        
    
    
    n,m,k=map(int,input().split())
    trie={}
    global case
    case=0
    for i in range(n):
        word=input()
        dct=trie
        for w in word:
            if w not in dct:
                dct[w]={}
            dct=dct[w]
        dct['#']=i+1
    d=dft(list)
    for i in range(m):
        
        word,idx=input().split()
        idx=int(idx)
        res=[]
        chk(word,trie,0)
        #print(res)
        temp=0
        for num in res:
            if num!=idx:
                d[idx].append(num)
            else:
                temp=1
        if not temp:
            case=1
    
    #print(d)
    
    order=[0]*(n+1)
    vis=[0]*(n+1)
    seen=set()
    idx=n
    
    for i in range(1,n+1):
        if not vis[i]:
            idx,tp=seq(i,idx)
            if tp:
                case=1
                break
    
    if case:
        print("NO")
    else:
        print("YES")
        print(*order[1:])
        
    


 
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
 
 
def print(*args, **kwargs):
    """Prints the values to a stream, or to sys.stdout by default."""
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start = True
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()

if sys.version_info[0] < 3:
    sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
else:
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
 
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
# endregion
 
 
if __name__ == "__main__":
    tc=1
    #tc = ii()
    for i in range(tc):
    	solve()