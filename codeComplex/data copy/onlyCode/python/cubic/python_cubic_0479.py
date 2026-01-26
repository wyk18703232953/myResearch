import os,sys,math 
from io import BytesIO, IOBase
from collections import defaultdict,deque,OrderedDict
import bisect as bi
def yes():print('YES')
def no():print('NO')
def I():return (int(input()))
def In():return(map(int,input().split()))
def ln():return list(map(int,input().split()))
def Sn():return input().strip()
BUFSIZE = 8192
#complete the main function with number of test cases to complete greater than x
def find_gt(a, x):
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:            
        return len(a)

def solve():
    n,m,k=In()
    rt,do=[[0]*m for i in range(n)],[[0]*m for i in range(n-1)]
    for i in range(n):
        z=list(In())
        for j in range(m-1):
            rt[i][j]=z[j]
    for i in range(n-1):
        z=list(In())
        for j in range(m):
            do[i][j]=z[j]

    dp=[[0]*m for i in range(n)]
    if k%2==1:
        for i in range(n):
            print(*[-1]*m)
        return
    k//=2
    for op in range(k):
        dp_next=[[P]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                ans=Inf
                if i!=0: 
                    ans=min(ans,dp[i-1][j]+do[i-1][j])
                if j!=0: 
                    ans=min(ans,dp[i][j-1]+rt[i][j-1])
                if i!=n-1:
                    ans = min( ans , dp[i+1][j]+do[i][j])
                if j!=m-1 : 
                    ans=min( ans , dp[i][j+1]+rt[i][j])
                dp_next[i][j]=ans

        for i in range(n):
            for j in range(m):
                dp[i][j]=dp_next[i][j]
            
    for i in range(n):
        for j in range(m):
            print(2*dp[i][j],end=' ')
        print()
        




def main():
    T=1
    for i in range(T):
        solve()
        
M = 998244353
P = 1000000007
Inf=float('inf')




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

if __name__ == '__main__':
    main()