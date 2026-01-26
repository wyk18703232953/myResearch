# link: https://codeforces.com/problemset/problem/961/C

import os, sys
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
input = lambda: sys.stdin.readline().rstrip("\r\n")
from math import ceil
mod = 10 ** 9 + 7 

def get_original_pieces(x):
    common = (pow(x, 2) - 1) // 2
    first_piece = "10"*common + '1'
    second_piece = '0' + "10"*common
    return [first_piece, second_piece]

# number of test cases
for _ in range(1):
    n = int(input())
    pieces = ["" for _ in range(4)]
    original_pieces = get_original_pieces(n)
    i = 0
    for _ in range(3 + (n*4)):
        s = input()
        if s:
            pieces[i] += s
        else:
            i += 1   
    #print(pieces) 
    till = pow(n, 2)
    fp = [[0,i] for i in range(4)]
    sp = [[0,i] for i in range(4)]
    for i in range(4):
        fpc, spc = 0, 0
        for j in range(till):
            if pieces[i][j] != original_pieces[0][j]:
                fpc += 1
            if pieces[i][j] != original_pieces[1][j]:
                spc += 1
        fp[i][0] = fpc
        sp[i][0] = spc
    fp.sort()
    sp.sort()
    ans1 = fp[0][0] + fp[1][0]
    ans2 = sp[0][0] + sp[1][0]
    for i in range(4):
        if sp[i][1] not in [fp[0][1], fp[1][1]]: ans1 += sp[i][0]
        if fp[i][1] not in [sp[0][1], sp[1][1]]: ans2 += fp[i][0]
    ans = min(ans1, ans2)
    print(ans)                            