def main(n):
    # n is the size of the n x n matrices
    # deterministically generate two n x n matrices of characters
    # First matrix: a[i][j] = chr((i + j) % 26 + 65) -> 'A'..'Z'
    a1_mat = [[chr((i + j) % 26 + 65) for j in range(n)] for i in range(n)]
    # Second matrix: apply a fixed pattern so complexity is comparable but data is deterministic
    # Here we construct a2 by rotating a1 once and then flipping horizontally,
    # which guarantees "Yes" for any n >= 1
    tmp_matrix = Matrix(n, n, a1_mat)
    tmp_matrix.rotate()
    tmp_matrix.fliph()
    a2_mat = tmp_matrix.mat

    a1, a2, ans = Matrix(n, n, a1_mat), Matrix(n, n, a2_mat), []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph()])
        a1.fliph()
    # print(['No', 'Yes'][a2.mat in ans])
    pass


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c
        if mat is not None:
            # deep copy via list comprehension to stay deterministic and simple
            self.mat = [row[:] for row in mat]

        else:
            self.mat = [[0 for _ in range(c)] for _ in range(r)]

    def rotate(self):
        mat0 = Matrix(self.c, self.r)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[j][self.r - (i + 1)] = self.mat[i][j]
        self.mat, self.r, self.c = [row[:] for row in mat0.mat], self.c, self.r
        return self.mat

    def flipv(self):
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[i][self.c - (j + 1)] = self.mat[i][j]
        self.mat = [row[:] for row in mat0.mat]
        return self.mat

    def fliph(self):
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[self.r - (i + 1)][j] = self.mat[i][j]
        self.mat = [row[:] for row in mat0.mat]
        return self.mat


if __name__ == "__main__":
    # example deterministic call for timing / scaling experiments
    main(300)