from copy import deepcopy
import random
import string


def main(n: int) -> bool:
    """
    生成规模为 n 的随机矩阵 a1 和 a2，
    判断 a2 是否可以通过 a1 的若干次旋转/翻转得到。
    返回 True 表示可以（原程序的 'Yes'），False 表示不可以（原程序的 'No'）。
    """
    # 生成测试数据：随机字符矩阵
    a1_data = random_matrix(n, n)
    # 为了有一定概率是可达的，这里先复制 a1，然后随机做若干次操作生成 a2
    a2_data = generate_related_matrix(a1_data)

    a1 = Matrix(n, n, a1_data)
    a2 = Matrix(n, n, a2_data)
    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])

    return a2.mat in ans


def random_matrix(r: int, c: int):
    # 使用大写字母生成随机矩阵
    letters = string.ascii_uppercase
    return [[random.choice(letters) for _ in range(c)] for _ in range(r)]


def generate_related_matrix(mat):
    # 以 mat 为基础，随机进行 0~10 次旋转/翻转，得到 a2
    m = Matrix(len(mat), len(mat[0]), mat)
    ops = [m.rotate, m.fliph, m.flipv]
    for _ in range(random.randint(0, 10)):
        random.choice(ops)()
    return deepcopy(m.mat)


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c
        if mat is not None:
            self.mat = deepcopy(mat)
        else:
            self.mat = [[0 for _ in range(c)] for _ in range(r)]

    def rotate(self):
        # 90 度顺时针旋转
        mat0 = Matrix(self.c, self.r)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[j][self.r - (i + 1)] = self.mat[i][j]
        self.mat, self.r, self.c = deepcopy(mat0.mat), self.c, self.r
        return self.mat

    def flipv(self):
        # 垂直翻转（左右镜像）
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[i][self.c - (j + 1)] = self.mat[i][j]
        self.mat = deepcopy(mat0.mat)
        return self.mat

    def fliph(self):
        # 水平翻转（上下镜像）
        mat0 = Matrix(self.r, self.c)
        for i in range(self.r):
            for j in range(self.c):
                mat0.mat[self.r - (i + 1)][j] = self.mat[i][j]
        self.mat = deepcopy(mat0.mat)
        return self.mat