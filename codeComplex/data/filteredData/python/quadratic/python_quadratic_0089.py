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
    # 生成 n×n 的字符矩阵，字符集可按需要调整
    chars = string.ascii_uppercase[:2]  # 例如只用 'A', 'B'，便于调试
    return [[random.choice(chars) for _ in range(n)] for _ in range(n)]


def apply_random_transform(mat):
    # 随机对矩阵做若干次旋转/翻转，用于生成可能相同的 a2
    m = Matrix(len(mat), len(mat[0]), mat)
    ops = [Matrix.rotate, Matrix.flipv, Matrix.fliph]
    for _ in range(random.randint(0, 5)):
        op = random.choice(ops)
        op(m)
    return deepcopy(m.mat)


def main(n: int):
    """
    n: 矩阵规模（n x n）
    逻辑与原程序相同：判断第二个矩阵是否能通过若干次旋转/翻转
    从第一个矩阵得到，并打印 'Yes' 或 'No'。
    测试数据自动生成：
      - a1 为随机字符矩阵
      - a2 有 50% 概率为 a1 的某种旋转/翻转结果，
        50% 概率为完全独立的随机矩阵
    """
    # 生成测试数据
    mat1 = gen_random_matrix_chars(n)
    a1 = Matrix(n, n, mat1)

    if random.random() < 0.5:
        # 生成一个与 a1 相关、可能匹配的矩阵
        mat2 = apply_random_transform(mat1)
    else:
        # 完全随机的另一个矩阵
        mat2 = gen_random_matrix_chars(n)

    a2 = Matrix(n, n, mat2)

    # 保持原逻辑：对 a1 进行一系列旋转、翻转，收集所有可能结果
    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])

    print(['No', 'Yes'][a2.mat in ans])


if __name__ == '__main__':
    # 示例：n=3，可根据需要更改或由外部调用 main(n)
    main(3)