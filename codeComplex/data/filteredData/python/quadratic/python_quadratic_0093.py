#!/usr/bin/python3

import copy
import random
import string


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


def main(n):
    # 生成一个 n×n 的随机矩阵 f 和由 f 经过随机变换得到的 g
    if n <= 0:
        return

    # 使用简单字符集，保证可见性
    chars = string.ascii_uppercase[:5]  # A-E

    # 随机生成原矩阵 f
    f = [[random.choice(chars) for _ in range(n)] for _ in range(n)]

    # 复制出 g 并施加随机变换（在原逻辑允许的变换空间内）
    g = copy.deepcopy(f)

    doflipv = random.randint(0, 1)
    dofliph = random.randint(0, 1)
    nrot = random.randint(0, 3)

    if dofliph == 1:
        g = fliphor(n, g)
    if doflipv == 1:
        g = flipver(n, g)
    for _ in range(nrot):
        g = rotate90(n, g)

    # 按原程序逻辑判断是否可以通过一系列变换从 f 得到 g
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
                    print("Yes")
                    return
    print("No")


if __name__ == "__main__":
    # 示例：使用 n=4 运行一次
    main(4)