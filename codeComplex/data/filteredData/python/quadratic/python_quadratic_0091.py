def main(n):
    # n 表示矩阵规模 n x n
    # 生成两个确定性的 n x n 字符矩阵
    a1_mat = [[chr(ord('a') + (i + j) % 26) for j in range(n)] for i in range(n)]
    # a2 是在 a1 上做一系列确定性变换后得到的矩阵
    # 为了让逻辑有真实运行路径，这里对 a1 做固定次数的操作
    a2_mat = [[a1_mat[i][j] for j in range(n)] for i in range(n)]
    a2 = Matrix(n, n, a2_mat)

    a1 = Matrix(n, n, a1_mat)
    ans = []
    for _ in range(4):
        ans.extend([a1.rotate(), a1.fliph(), a1.flipv(), a1.fliph(), a1.flipv()])
    result = ['No', 'Yes'][a2.mat in ans]
    # print(result)
    pass


class Matrix:
    def __init__(self, r, c, mat=None, id=None):
        self.r, self.c = r, c
        if mat is not None:
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
    # 示例调用：可根据需要修改 n 以做规模实验
    main(5)