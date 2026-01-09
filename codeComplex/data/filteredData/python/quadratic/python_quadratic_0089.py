import sys
from copy import deepcopy


def main(n):
    # Interpret n as matrix size n x n
    # Deterministic generation of two matrices a1 and a2 consisting of '0' and '1' characters
    # a1: pattern based on (i + j) % 2
    # a2: pattern based on (i * j) % 2
    def gen_mat1(size):
        return [[('1' if (i + j) % 2 == 0 else '0') for j in range(size)] for i in range(size)]

    def gen_mat2(size):
        return [[('1' if (i * j) % 2 == 0 else '0') for j in range(size)] for i in range(size)]

    a1 = Matrix(n, n, gen_mat1(n))
    a2 = Matrix(n, n, gen_mat2(n))
    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])
    res = ['No', 'Yes'][a2.mat in ans]
    # Keep some work dependent on n to avoid optimization-away in experiments
    sys.stdout.write(res + "\n")


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c

        if mat is not None:
            self.mat = deepcopy(mat)

        else:
            self.mat = [[0 for _ in range(c)] for _ in range(r)]

            if id is not None:
                for i in range(r):
                    self.mat[i][i] = 1

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


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(5)