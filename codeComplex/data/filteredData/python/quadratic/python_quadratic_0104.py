import random
import string


def rotate(li, n):
    newli = [row.copy() for row in li]
    for x in range(n):
        for y in range(n):
            newli[x][y] = li[n - 1 - y][x]
    return newli


def flipV(li, n):
    newli = [row.copy() for row in li]
    newli.reverse()
    return newli


def flipH(li, n):
    newli = [row.copy() for row in li]
    for x in range(n):
        newli[x].reverse()
    return newli


def main(n):
    # 生成 n×n 的随机字符矩阵 li1
    chars = string.ascii_uppercase
    li1 = [[random.choice(chars) for _ in range(n)] for _ in range(n)]

    # 通过随机变换从 li1 生成 li2，保证两矩阵有一定关系
    li2 = [row.copy() for row in li1]
    transforms = [
        "identical",
        "flipH",
        "flipV",
        "rot1",
        "rot2",
        "rot3",
        "flipH_rot1",
        "flipH_rot2",
        "flipH_rot3",
    ]
    t = random.choice(transforms)

    if t == "flipH":
        li2 = flipH(li2, n)
    elif t == "flipV":
        li2 = flipV(li2, n)
    elif t == "rot1":
        li2 = rotate(li2, n)
    elif t == "rot2":
        li2 = rotate(rotate(li2, n), n)
    elif t == "rot3":
        li2 = rotate(rotate(rotate(li2, n), n), n)
    elif t == "flipH_rot1":
        li2 = rotate(flipH(li2, n), n)
    elif t == "flipH_rot2":
        li2 = rotate(rotate(flipH(li2, n), n), n)
    elif t == "flipH_rot3":
        li2 = rotate(rotate(rotate(flipH(li2, n), n), n), n)
    # "identical" 情况下 li2 已经是 li1 的拷贝

    # 以下为原逻辑，只是用生成的 li1、li2
    li3, templi = [], []

    # identical
    if li1 == li2:
        print("Yes")
        return

    # flip horizontal
    templi = flipH(li2, n)
    if li1 == templi:
        print("Yes")
        return

    # flip vertical
    templi = flipV(li2, n)
    if li1 == templi:
        print("Yes")
        return

    # rotate1
    templi = rotate(li2, n)
    if li1 == templi:
        print("Yes")
        return

    # rotate2
    templi = rotate(templi, n)
    if li1 == templi:
        print("Yes")
        return

    # rotate3
    templi = rotate(templi, n)
    if li1 == templi:
        print("Yes")
        return

    # flipH + rotations
    templi = flipH(li2, n)
    templi = rotate(templi, n)
    if li1 == templi:
        print("Yes")
        return

    templi = rotate(templi, n)
    if li1 == templi:
        print("Yes")
        return

    templi = rotate(templi, n)
    if li1 == templi:
        print("Yes")
        return

    print("No")