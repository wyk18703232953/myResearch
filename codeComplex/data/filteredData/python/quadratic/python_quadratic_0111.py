import copy
import random


def generate_matrix(a):
    # 随机生成 a×a 的矩阵，元素为 '0' 或 '1'
    return [[random.choice(['0', '1']) for _ in range(a)] for _ in range(a)]


def equal_matrix(m1, m2, a):
    for i in range(a):
        for j in range(a):
            if m1[i][j] != m2[i][j]:
                return False
    return True


def rotate90(src, dst, a):
    # 顺时针旋转90°
    for i in range(a):
        for j in range(a):
            dst[a - 1 - j][i] = src[i][j]


def rotate180(src, dst, a):
    for i in range(a):
        for j in range(a):
            dst[a - 1 - i][a - 1 - j] = src[i][j]


def rotate270(src, dst, a):
    for i in range(a):
        for j in range(a):
            dst[j][a - 1 - i] = src[i][j]


def flip_horizontal(src, a):
    # 水平翻转（左右翻面）
    listtemp = copy.deepcopy(src)
    for i in range(a):
        for j in range(a):
            src[i][j] = listtemp[i][a - 1 - j]


def main(n):
    a = n
    # 1. 生成测试数据：随机生成两个矩阵 lista、listb
    lista = generate_matrix(a)
    listb = generate_matrix(a)

    flag = 0

    # 为了和原始代码逻辑保持一致，从这里开始基本照搬原逻辑

    listacpy = copy.deepcopy(lista)

    # 一来就比（不变换）
    if equal_matrix(listacpy, listb, a):
        flag = 1

    # 转90°
    if flag == 0:
        rotate90(lista, listacpy, a)
        if equal_matrix(listacpy, listb, a):
            flag = 1

    # 转180°
    if flag == 0:
        rotate180(lista, listacpy, a)
        if equal_matrix(listacpy, listb, a):
            flag = 1

    # 转270°
    if flag == 0:
        rotate270(lista, listacpy, a)
        if equal_matrix(listacpy, listb, a):
            flag = 1

    # 翻面
    if flag == 0:
        flip_horizontal(lista, a)

        # 翻面后直接比
        listacpy = copy.deepcopy(lista)
        if equal_matrix(listacpy, listb, a):
            flag = 1

        # 翻面后转90°
        if flag == 0:
            rotate90(lista, listacpy, a)
            if equal_matrix(listacpy, listb, a):
                flag = 1

        # 翻面后转180°
        if flag == 0:
            rotate180(lista, listacpy, a)
            if equal_matrix(listacpy, listb, a):
                flag = 1

        # 翻面后转270°
        if flag == 0:
            rotate270(lista, listacpy, a)
            if equal_matrix(listacpy, listb, a):
                flag = 1

    if flag == 1:
        print("yes")
    else:
        print("no")


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)