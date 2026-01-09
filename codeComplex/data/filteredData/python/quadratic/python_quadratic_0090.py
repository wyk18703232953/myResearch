def main(n):
    # Generate a deterministic n x n matrix of characters
    # Use a simple pattern: chr(97 + (i+j) % 26) -> 'a'..'z'
    a1_mat = [[chr(97 + (i + j) % 26) for j in range(n)] for i in range(n)]
    # Let a2 be a fixed transformation of a1 to keep structure similar
    # For determinism, we choose a2 as the result of rotating a1 once
    a1 = Matrix(n, n, a1_mat)
    a2 = Matrix(n, n, a1_mat)
    a2.rotate()  # a2 becomes one rotation of original a1
    a2_mat_snapshot = [row[:] for row in a2.mat]  # snapshot to avoid later in-place changes

    # Now reproduce the original main-logic using fresh Matrix objects
    a1 = Matrix(n, n, a1_mat)
    a2 = Matrix(n, n, a2_mat_snapshot)
    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])
    result = ['No', 'Yes'][a2.mat in ans]
    # print(result)
    pass


from copy import deepcopy


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c
        if mat is not None:
            self.mat = deepcopy(mat)

        else:
            self.mat = [[0 for _ in range(c)] for _ in range(r)]

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
    # Example fixed-size call for experimentation
    main(5)