import os
import sys
from io import BytesIO, IOBase


def main():
    n,m,k=map(int,input().split())
    if (k%2==0):
        DP=[[[10**9 for i in range(m)] for j in range(n)] for v in range(k//2)]
        A=[]
        B=[]
        for i in range(n):
            L=list(map(int,input().split()))
            A.append(L)
            for j in range(m-1):
                DP[0][i][j]=min(DP[0][i][j],L[j])
                DP[0][i][j+1]=min(L[j],DP[0][i][j+1])
                
        for i in range(n-1):
            L=list(map(int,input().split()))
            B.append(L)
            for j in range(m):
                DP[0][i][j]=min(DP[0][i][j],L[j])
                DP[0][i+1][j]=min(DP[0][i+1][j],L[j])
    
        for k1 in range(1,k//2):
            for i in range(n):
                for j in range(m):
                    if (i>0):
                        DP[k1][i][j]=min(DP[k1][i][j],B[i-1][j]+DP[k1-1][i-1][j])
                    if (j>0):
                        DP[k1][i][j]=min(DP[k1][i][j],A[i][j-1]+DP[k1-1][i][j-1])
                    if (i<(n-1)):
                        DP[k1][i][j]=min(DP[k1][i][j],B[i][j]+DP[k1-1][i+1][j])
                    if (j<(m-1)):
                        DP[k1][i][j]=min(DP[k1][i][j],A[i][j]+DP[k1-1][i][j+1])
                
        for val in DP[(k//2)-1]:
            ans=[i*2 for i in val]
            print(*ans)
    
    else:
        for i in range(n):
            L=list(map(int,input().split()))
        
        for i in range(n-1):
            L=list(map(int,input().split()))
        
        for i in range(n):
            ans=[-1]*m
            print(*ans)



# region fastio

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
    main()
