# -*- coding: utf-8 -*-

from itertools import accumulate
import random

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    return int(-(-x // y))

INF = 10 ** 18
MOD = 10 ** 9 + 7

def build_grid_from_data(H, W, rows, intv, _type, space=True, padding=False):
    # rows: list of strings representing the grid
    if space:
        _input = lambda s: s.split()
    else:
        _input = lambda s: s
    _list = lambda s: list(map(_type, _input(s)))
    offset = 1 if padding else 0
    grid = list2d(H + offset * 2, W + offset * 2, intv)
    for i in range(offset, H + offset):
        row = _list(rows[i - offset])
        for j in range(offset, W + offset):
            grid[i][j] = row[j - offset]
    return grid

def main(n):
    # 1. 根据 n 生成测试数据：生成一个大致为 n*n 的随机网格
    # 为避免过大，限制尺寸在 1..n（至少为 1）
    H = max(1, n)
    W = max(1, n)

    # 随机生成由 '.' 和 '*' 组成的 H x W 网格
    rows = []
    for _ in range(H):
        row = ''.join(random.choice(['.', '*']) for _ in range(W))
        rows.append(row)

    # 2. 原逻辑开始：使用 padding=1 的字符网格
    grid = build_grid_from_data(H, W, rows, '#', str, space=False, padding=True)

    ans = []
    imosw = list2d(H + 2, W + 2, 0)
    imosh = list2d(H + 2, W + 2, 0)

    L = list2d(H + 2, W + 2, 0)
    R = list2d(H + 2, W + 2, 0)
    U = list2d(H + 2, W + 2, 0)
    D = list2d(H + 2, W + 2, 0)

    def check(i, j):
        sz = min(L[i][j], R[i][j], U[i][j], D[i][j])
        if sz > 1:
            imosw[i][j - sz + 1] += 1
            imosw[i][j + sz] -= 1
            imosh[i - sz + 1][j] += 1
            imosh[i + sz][j] -= 1
            ans.append((i, j, sz - 1))

    def check2():
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                if grid[i][j] == '*' and not imosw[i][j] and not imosh[i][j]:
                    return False
        return True

    # 计算 L（向左连续'*'长度）
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '.':
                L[i][j] = 0
            else:
                L[i][j] = L[i][j - 1] + 1

    # 计算 R（向右连续'*'长度）
    for i in range(1, H + 1):
        for j in range(W, 0, -1):
            if grid[i][j] == '.':
                R[i][j] = 0
            else:
                R[i][j] = R[i][j + 1] + 1

    # 计算 U（向上连续'*'长度）
    for j in range(1, W + 1):
        for i in range(1, H + 1):
            if grid[i][j] == '.':
                U[i][j] = 0
            else:
                U[i][j] = U[i - 1][j] + 1

    # 计算 D（向下连续'*'长度）
    for j in range(1, W + 1):
        for i in range(H, 0, -1):
            if grid[i][j] == '.':
                D[i][j] = 0
            else:
                D[i][j] = D[i + 1][j] + 1

    # 枚举中心，尝试形成十字
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '*':
                check(i, j)

    # 横向 imos
    for i in range(1, H + 1):
        for j in range(W + 1):
            imosw[i][j + 1] += imosw[i][j]

    # 纵向 imos
    for j in range(1, W + 1):
        for i in range(H + 1):
            imosh[i + 1][j] += imosh[i][j]

    # 输出结果（与原程序相同格式）
    if check2():
        print(len(ans))
        for h, w, sz in ans:
            print(h, w, sz)
    else:
        print(-1)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)