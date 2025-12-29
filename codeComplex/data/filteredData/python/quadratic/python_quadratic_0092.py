from copy import deepcopy
import random
import string


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


def gen_matrix(n, alphabet="01"):
    # 生成 n×n 的随机字符矩阵
    return [[random.choice(alphabet) for _ in range(n)] for _ in range(n)]


def main(n):
    # 根据 n 生成测试数据
    a1_mat = gen_matrix(n)
    a2_mat = gen_matrix(n)

    a1 = Matrix(n, n, a1_mat)
    a2 = Matrix(n, n, a2_mat)

    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph()])
        a1.fliph()

    result = ['No', 'Yes'][a2.mat in ans]
    print(result)
    return result