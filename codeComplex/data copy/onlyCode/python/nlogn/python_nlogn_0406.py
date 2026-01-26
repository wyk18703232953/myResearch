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
    n=I()
    points,l=[],[]
    for i in range(n):
        a,b=In()
        l.append((a,b))
        points.append(a)
        points.append(b)
    points.sort()
    k=0 
    d={}
    l1=[]
    for i in range(2*n):
        if d.get(points[i],-1)==-1:
            d[points[i]]=k
            l1.append(points[i])
            k+=1
    # print(l1)
    n1=len(d)
    dp=[[0,0] for i in range(n1)]
    for a,b in l:
        dp[d[a]][0]+=1
        dp[d[b]][1]-=1

    ans={}
    last=dp[0][0]
    ans[last]=1
    last+=dp[0][1]
    for i in range(1,n1):
        cnts=l1[i]-l1[i-1]-1
        if ans.get(last,-1)!=-1:
            ans[last]+=cnts
        else:
            ans[last]=cnts
        last+=dp[i][0]
        if ans.get(last,-1)!=-1:
            ans[last]+=1
        else:
            ans[last]=1
        last+=dp[i][1]
    if ans.get(last,-1)!=-1:
        ans[last]+=1
    else:
        ans[last]=1
    for i in range(1,n+1):
        print(ans.get(i,0),end=' ')
    print()
    pass
def main():
    T=1
    for i in range(T):
        solve()
        
M = 998244353
P = 1000000007
 




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