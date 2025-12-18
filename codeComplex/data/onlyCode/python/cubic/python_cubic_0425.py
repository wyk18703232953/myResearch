# Author : nitish420 --------------------------------------------------------------------
import os
import sys
from io import BytesIO, IOBase
# mod=10**9+7
# sys.setrecursionlimit(10**5)
mxm=sys.maxsize

def solve(p,q,r):

    if p<0 or p>=n or q<0 or q>=m:
        return mxm

    if dp[r][p][q]!=-1:
        return dp[r][p][q]


    if r==0:
        return 0

    z=int()
    a,b,c,d=0,0,0,0
    a=dp[r-1][p][q-1]
    b=dp[r-1][p][q+1]
    c=dp[r-1][p-1][q]
    d=dp[r-1][p+1][q]

    if a==-1:
        a=row[p][q-1]+solve(p,q-1,r-1)
    else:
        a+=row[p][q-1]

    if b==-1:
        b=row[p][q]+solve(p,q+1,r-1)
    else:
        b+=row[p][q]
    
    if c==-1:
        c=col[p-1][q]+solve(p-1,q,r-1)
    else:
        c+=col[p-1][q]
    
    if d==-1:
        d=col[p][q]+solve(p+1,q,r-1)
    else:
        d+=col[p][q]



    z=min([a,b,c,d])

    dp[r][p][q]=z
    return z


n,m,k=map(int,input().split())
row=[]
col=[]
for i in range(n):

    row.append(list(map(int,input().split()))+[0])

for _ in range(n-1):

    col.append(list(map(int,input().split())))


col.append([0 for i in range(m)])

ans=[[-1 for _ in range(m)] for _ in range(n)]

dp=[[[-1 for _ in range(m+1)] for _ in range(n+1)] for _ in range(k+1)]

def main():

    if k%2:
        for item in ans:
            print(*item)
        exit()

    
    for r in range(n):
        for c in range(m):
            ans[r][c]=2*solve(r,c,k//2)
    
    for item in ans:
        print(*item)




#----------------------------------------------------------------------------------------
def nouse0():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')
def nouse1():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')
def nouse2():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')




# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
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
            self.newlines = b.count(b'\n') + (not b)
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
        self.write = lambda s: self.buffer.write(s.encode('ascii'))
        self.read = lambda: self.buffer.read().decode('ascii')
        self.readline = lambda: self.buffer.readline().decode('ascii')


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')




def nouse3():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')
def nouse4():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')
def nouse5():
    # This is to save my code from plag due to use of FAST IO template in it.
    a=420
    b=420
    print(f'i am nitish{(a+b)//2}')



# endregion

if __name__ == '__main__':
    main()