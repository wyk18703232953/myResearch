import os
import sys
from io import BytesIO, IOBase
from collections import Counter

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


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main():
    # for _ in range(int(input())):
    #     # =int(input())
    #     # =input()
    #     # =list(map(int, input().split()))
    #     # =map(int, input().split())
    n=int(input())
    a=[]
    for i in range(n):
        a.append(list(map(int, input().split())))
    d={}
    if n==1:
        print('YES')
        return
    vis=[0]*n
    for i in range(1,n):
        num=abs(a[i][1]-a[0][1])
        den=abs(a[i][0]-a[0][0])
        k=1
        k=gcd(num, den)
        num//=k
        den//=k
        if ((a[i][1]-a[0][1])*(a[i][0]-a[0][0]))<0:
            num*=-1
        if (num, den) in d:
            d[(num, den)].append(i)
        else:
            d[(num, den)]=[i]
    maxx=0
    #print(d)
    for i in d.keys():
        if len(d[i])>maxx:
            maxx=len(d[i])
            ki=i
    vis[0]=1
    for i in d[ki]:
        vis[i]=1
    t=[]
    for i in range(n):
        if not vis[i]:
            t.append(i)
    f=1
    if len(t)>1:
        num=abs(a[t[0]][1]-a[t[1]][1])
        den=abs(a[t[0]][0]-a[t[1]][0])
        k = 1
        k=gcd(num, den)
        num//=k
        den//=k
        if (a[t[0]][1]-a[t[1]][1])*(a[t[0]][0]-a[t[1]][0])<0:
            num*=-1
        m=(num, den)
        for i in range(2, len(t)):
            num = abs(a[t[i]][1] - a[t[0]][1])
            den = abs(a[t[i]][0] - a[t[0]][0])
            k=gcd(num, den)
            num //= k
            den //= k
            if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                num *= -1
            if (num,den)!=m:
                f=0
    if f:
        print('YES')
    else:
        d = {}
        if n == 1:
            print('YES')
            return
        vis = [0] * n
        a[0], a[1]=a[1], a[0]
        for i in range(1, n):
            num = abs(a[i][1] - a[0][1])
            den = abs(a[i][0] - a[0][0])
            k = 1
            k = gcd(num, den)
            num //= k
            den //= k
            if ((a[i][1] - a[0][1]) * (a[i][0] - a[0][0])) < 0:
                num *= -1
            if (num, den) in d:
                d[(num, den)].append(i)
            else:
                d[(num, den)] = [i]
        maxx = 0
        #print(d)
        for i in d.keys():
            if len(d[i]) > maxx:
                maxx = len(d[i])
                ki = i
        vis[0] = 1
        for i in d[ki]:
            vis[i] = 1
        t = []
        for i in range(n):
            if not vis[i]:
                t.append(i)
        f = 1
        if len(t) > 1:
            num = abs(a[t[0]][1] - a[t[1]][1])
            den = abs(a[t[0]][0] - a[t[1]][0])
            k = 1
            k=gcd(num, den)
            num //= k
            den //= k
            if (a[t[0]][1] - a[t[1]][1]) * (a[t[0]][0] - a[t[1]][0]) < 0:
                num *= -1
            m = (num, den)
            for i in range(2, len(t)):
                num = abs(a[t[i]][1] - a[t[0]][1])
                den = abs(a[t[i]][0] - a[t[0]][0])
                k = 1
                k=gcd(num, den)
                num //= k
                den //= k
                if (a[t[0]][1] - a[t[i]][1]) * (a[t[0]][0] - a[t[i]][0]) < 0:
                    num *= -1
                if (num, den) != m:
                    f = 0
        if f:
            print('YES')
        else:
            print('NO')








    return


if __name__ == "__main__":
    main()