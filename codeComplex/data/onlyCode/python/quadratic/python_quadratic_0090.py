import os, sys
from io import BytesIO, IOBase
from copy import deepcopy


def main():
    n = rint()
    a1, a2, ans = Matrix(n, n, rstr_2d(n)), Matrix(n, n, rstr_2d(n)), []
    for i in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])
    print(['No', 'Yes'][a2.mat in ans])


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c

        if mat != None:
            self.mat = deepcopy(mat)
        else:
            self.mat = [[0 for i in range(c)] for j in range(r)]

    def __add__(self, other):
        mat0 = Matrix(self.r, self.c)

        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[i][j] = self.mat[i][j] + other.mat[i][j]

        return mat0

    def __mul__(self, other):
        mat0 = Matrix(self.r, other.c)

        for i in range(self.r):
            for j in range(other.c):
                for k in range(self.c):
                    mat0.mat[i][j] += self.mat[i][k] * other.mat[k][j]

        return mat0

    def dot_mul(self, other):
        res = 0
        for i in range(self.r):
            for j in range(self.c):
                res += self.mat[i][j] * other.mat[j][i]

        return res

    def trace(self):
        res = 0
        for i in range(self.r):
            res += self.mat[i][i]

        return res

    def rotate(self):
        mat0 = Matrix(self.c, self.r)

        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[j][self.r - (i + 1)] = self.mat[i][j]

        self.mat, self.r, self.c = deepcopy(mat0.mat), self.c, self.r
        return self.mat

    def flipv(self):
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[i][self.c - (j + 1)] = self.mat[i][j]

        self.mat = deepcopy(mat0.mat)
        return self.mat

    def fliph(self):
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[self.r - (i + 1)][j] = self.mat[i][j]

        self.mat = deepcopy(mat0.mat)
        return self.mat

    def mat_pow(self, mat, p, mod=None):
        sq = Matrix(mat.r, mat.r, id=1)

        while p:
            if p & 1:
                p -= 1
                sq = sq * mat

            p //= 2
            mat = mat * mat

        return sq.mat


# FASTIO REGION
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


BUFSIZE = 8192
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
rstr = lambda: input().strip()
rstrs = lambda: [str(x) for x in input().split()]
rstr_2d = lambda n: [list(rstr()) for _ in range(n)]
rint = lambda: int(input())
rints = lambda: [int(x) for x in input().split()]
rint_2d = lambda n: [rint() for _ in range(n)]
rints_2d = lambda n: [rints() for _ in range(n)]
ceil1 = lambda a, b: (a + b - 1) // b

if __name__ == '__main__':
    main()
