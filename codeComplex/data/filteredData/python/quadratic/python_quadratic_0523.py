#!/usr/bin/env python

import random


def check(m, v, x, y):
    # 如果 x,y 为中心的 3x3 内除了中心以外全部为 True，则标记这些为可覆盖
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) == (0, 0):
                continue
            if not m[x + i][y + j]:
                return

    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if (i, j) != (0, 0):
                v[x + i][y + j] = True


def main(n):
    """
    n: 规模参数，用来生成一个 n x n 的测试矩阵。
       '#' 和 '.' 随机生成，其中 '#' 表示 True，'.' 表示 False。
    函数打印 "YES" 或 "NO"。
    """
    if n <= 0:
        print("NO")
        return

    # 随机生成 n x n 的字符矩阵，'#' 概率可以调整
    m = n  # 使用方阵，列数 = 行数 = n
    mat = []
    v = []
    for _ in range(n):
        row = [random.random() < 0.4 for _ in range(m)]  # 40% 概率为 '#'
        mat.append(row)
        v.append([False] * m)

    # 核心逻辑：与原题一致
    for x in range(1, n - 1):
        for y in range(1, m - 1):
            check(mat, v, x, y)

    flag = True
    for i in range(n):
        for j in range(m):
            if mat[i][j] and (not v[i][j]):
                flag = False

    if flag:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)