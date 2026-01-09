def main(n):
    # n is the matrix size (n x n), and also implicitly defines both matrices.
    # Deterministically generate two n x n matrices of characters '0'..'9'.
    def gen_matrix(size, offset):
        # offset differentiates the two matrices but keeps determinism
        return [[str((i * size + j + offset) % 10) for j in range(size)] for i in range(size)]

    a1 = Matrix(n, n, gen_matrix(n, 0))
    a2 = Matrix(n, n, gen_matrix(n, 1))

    # Core logic from original main, without I/O or early exit
    ans = "No"
    for _ in range(4):
        if a2.mat in [a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()]:
            ans = "Yes"
            break
    # print(ans)
    pass


from copy import deepcopy


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
                s = 0
                for k in range(self.c):
                    s += self.mat[i][k] * other.mat[k][j]
                mat0.mat[i][j] = s
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
    # Example deterministic call for testing / benchmarking
    main(5)