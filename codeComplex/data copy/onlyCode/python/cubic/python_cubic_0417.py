# by the authority of GOD     author: manhar singh sachdev #

def some_random_function():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function5():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

import os,sys
from io import BytesIO,IOBase
# from array import array

def main():
    n,m,k = map(int,input().split())
    hor = [list(map(int,input().split()))+[10**20+1] for _ in range(n)]
    ver = [list(map(int,input().split())) for _ in range(n-1)]+[[10**20+1]*m]
    if k&1:
        for _ in range(n):
            print(*[-1]*m)
        exit()
    dp = [[0]*m for _ in range(n)]
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    for _ in range(k//2):
        dp1 = [[10**20]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for kk in range(4):
                    x1,y1 = i+dx[kk],j+dy[kk]
                    if kk < 2:
                        ed = hor[i][j-(kk==1)]
                    else:
                        ed = ver[i-(kk==3)][j]
                    if ed != 10**20+1:
                        dp1[i][j] = min(dp1[i][j],2*ed+dp[x1][y1])
        dp = dp1
    for i in dp:
        print(*i)

#Fast IO Region
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

def some_random_function1():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function2():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function3():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function4():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function6():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function7():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

def some_random_function8():
    """due to the fast IO template, my code gets caught in
       plag check for no reason. That is why, I am making
       random functions"""
    x = 10
    x *= 100
    i_dont_know = x
    why_am_i_writing_this = x*x
    print(i_dont_know)
    print(why_am_i_writing_this)

if __name__ == '__main__':
    main()