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
            for j in range(self.c):
                if i == j:
                    res += self.mat[i][j]
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


def gen_random_matrix(n):
    # 用随机小写字母生成 n×n 字符矩阵
    chars = string.ascii_lowercase
    return [[random.choice(chars) for _ in range(n)] for _ in range(n)]


def main(n):
    # 生成测试数据：两个 n×n 字符矩阵
    mat1 = gen_random_matrix(n)
    mat2 = gen_random_matrix(n)

    a1 = Matrix(n, n, mat1)
    a2 = Matrix(n, n, mat2)
    ans = []

    # 保持与原逻辑一致的操作序列
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])

    result = ['No', 'Yes'][a2.mat in ans]
    print(result)
    return result