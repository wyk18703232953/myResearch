import sys
from copy import deepcopy


def generate_matrix(n):
    # Deterministically generate an n x n matrix of '0'/'1' characters
    # Example pattern: element (i, j) = (i * n + j) % 2
    return [[str((i * n + j) % 2) for j in range(n)] for i in range(n)]


def main(n):
    # n is the matrix dimension
    if n <= 0:
        print("No")
        return

    a1_mat = generate_matrix(n)
    a2_mat = generate_matrix(n)

    a1 = Matrix(n, n, a1_mat)
    a2 = Matrix(n, n, a2_mat)

    for _ in range(4):
        if a2.mat in [a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()]:
            print("Yes")
            return
    print("No")


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
    # Example deterministic call for experimentation
    main(5)