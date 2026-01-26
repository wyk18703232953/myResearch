import sys
from copy import deepcopy


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c
        if mat is not None:
            self.mat = deepcopy(mat)

        else:
            self.mat = [[0 for _ in range(c)] for _ in range(r)]

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


def generate_matrix(n, offset):
    # Deterministic generation: use characters from 'A'.. with offset
    mat = []
    for i in range(n):
        row = []
        for j in range(n):
            val = (i * n + j + offset) % 26
            row.append(chr(ord('A') + val))
        mat.append(row)
    return mat


def main(n):
    # n is the matrix dimension (n x n)
    if n <= 0:
        # print("No")
        pass
        return

    base_mat = generate_matrix(n, 0)
    # a1 is the original matrix
    a1 = Matrix(n, n, base_mat)

    # Construct a2 deterministically from a1 so algorithm still does meaningful work
    # Here we choose a2 as the result of applying rotate, fliph, flipv once in sequence
    temp_matrix = Matrix(n, n, base_mat)
    temp_matrix.rotate()
    temp_matrix.fliph()
    temp_matrix.flipv()
    a2 = Matrix(n, n, temp_matrix.mat)

    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])

    # print(['No', 'Yes'][a2.mat in ans])
    pass
if __name__ == "__main__":
    # Example deterministic calls for experimentation
    # You can change these ns or loop over many ns in your experiments
    main(3)
    main(5)