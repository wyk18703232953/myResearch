from collections import defaultdict
import bisect
from itertools import accumulate, count
import os
import sys
import math
from io import BytesIO, IOBase

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


def input(): return sys.stdin.readline().rstrip("\r\n")



# ------------------- fast io --------------------
s=input()
neg=0
if int(s)<0:
    neg=1
ans1 = ""
s=int(s)
s=abs(s)
s=str(s)
ans2 = ""
for i in range(0, len(s)):
    if i == len(s)-2:
        ans1 += s[i]
    elif i == len(s)-1:
        ans2 += s[i]
    else:
        ans1 += s[i]
        ans2 += s[i]
if neg==0:
    print(s)
else:
    if str(min(int(ans1), int(ans2)))=="0":
        print(0)
    else:
        print("-"+str(min(int(ans1), int(ans2))))
