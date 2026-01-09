#!/usr/bin/python3

import copy


def rotate90(n, f):
    return [[f[n - j - 1][i] for j in range(n)] for i in range(n)]

def fliphor(n, f):
    return [[f[i][n - j - 1] for j in range(n)] for i in range(n)]

def flipver(n, f):
    return [[f[n - i - 1][j] for j in range(n)] for i in range(n)]

def eq(n, f, g):
    for i in range(n):
        for j in range(n):
            if f[i][j] != g[i][j]:
                return False
    return True

def generate_matrix(n, offset):
    # 生成一个 n x n 的字符矩阵，使用确定性规则
    # 字符从 'A' ~ 'Z' 循环
    return [[chr(ord('A') + ((i * n + j + offset) % 26)) for j in range(n)] for i in range(n)]

def main(n):
    # n 作为矩阵的规模：n x n
    if n <= 0:
        return

    # 生成原矩阵 f
    f = generate_matrix(n, 0)

    # 生成目标矩阵 g：对 f 做一组确定的变换
    # 为了保证可扩展性，这里用确定性的规则选择变换：
    # doflipv, dofliph, nrot 由 n 决定
    doflipv = (n // 2) % 2       # 0 或 1
    dofliph = (n // 3) % 2       # 0 或 1
    nrot = n % 4                 # 0~3

    g = copy.deepcopy(f)
    if dofliph == 1:
        g = fliphor(n, g)
    if doflipv == 1:
        g = flipver(n, g)
    for _ in range(nrot):
        g = rotate90(n, g)

    # 保持原有的核心判定逻辑
    for doflipv_try in range(2):
        for dofliph_try in range(2):
            for nrot_try in range(4):
                h = copy.deepcopy(f)
                if dofliph_try == 1:
                    h = fliphor(n, h)
                if doflipv_try == 1:
                    h = flipver(n, h)
                for _ in range(nrot_try):
                    h = rotate90(n, h)
                if eq(n, h, g):
                    # print("Yes")
                    pass
                    return

    # print("No")
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 规模
    main(5)