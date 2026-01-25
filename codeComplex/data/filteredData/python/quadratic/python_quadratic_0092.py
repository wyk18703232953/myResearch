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


def main(n):
    if n <= 0:
        print("No")
        return

    # Deterministically generate two n x n matrices of characters
    # a1: pattern based on (i + j) % 3
    # a2: another pattern based on (i * j) % 3
    chars = ["0", "1", "2"]
    mat1 = [[chars[(i + j) % 3] for j in range(n)] for i in range(n)]
    mat2 = [[chars[(i * j) % 3] for j in range(n)] for i in range(n)]

    a1 = Matrix(n, n, mat1)
    a2 = Matrix(n, n, mat2)
    ans = []

    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph()])
        a1.fliph()

    print(["No", "Yes"][a2.mat in ans])


if __name__ == "__main__":
    # Example call for deterministic experiment; adjust n as needed
    main(5)