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


def gen_random_matrix_chars(n):
    # 生成一个 n×n 的字符矩阵，字符从 '0'-'1' 或 '0'-'9','A'-'Z' 中选
    alphabet = "01"
    # 如需更多字符，可以改为：
    # alphabet = string.digits + string.ascii_uppercase
    return [[random.choice(alphabet) for _ in range(n)] for _ in range(n)]


def main(n):
    # 生成测试数据
    mat1 = gen_random_matrix_chars(n)
    mat2 = deepcopy(mat1)

    # 随机对 mat2 做若干次变换（旋转/翻转），也可能不变
    m2 = Matrix(n, n, mat2)
    ops = [m2.rotate, m2.fliph, m2.flipv]
    for _ in range(random.randint(0, 4)):
        random.choice(ops)()

    a1 = Matrix(n, n, mat1)
    a2 = Matrix(n, n, m2.mat)

    # 保持原逻辑：检查 a2 是否能通过旋转/翻转与 a1 一致
    for _ in range(4):
        if a2.mat in [a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()]:
            print("Yes")
            return
    print("No")