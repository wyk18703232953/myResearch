import random

def main(n: int):
    # 随机生成一个 n x n 的矩阵，包含 '.' 和 'B'
    # 为保证有解，随机生成一个连续的 B 方块（至少 1x1）
    m = n
    li = [['.' for _ in range(m)] for _ in range(n)]

    # 随机确定一个 B 方块区域
    top = random.randint(0, n - 1)
    left = random.randint(0, m - 1)
    bottom = random.randint(top, n - 1)
    right = random.randint(left, m - 1)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            li[i][j] = 'B'

    position1 = 0
    position2 = 0
    position3 = 0
    position4 = 0

    # 从左往右找第一列包含 B 的列，并记录该列中第一个 B 的行号
    for j in range(m):
        flag = False
        for i in range(n):
            if li[i][j] == "B":
                flag = True
                position1 = i
                break
        if flag:
            break

    # 从右往左找第一列包含 B 的列，并记录该列中最后一个 B 的行号
    for j in range(m - 1, -1, -1):
        flag = False
        for i in range(n - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position2 = i
                break
        if flag:
            break

    # 从上往下找第一行包含 B 的行，并记录该行中第一个 B 的列号
    for i in range(n):
        flag = False
        for j in range(m):
            if li[i][j] == "B":
                flag = True
                position3 = j
                break
        if flag:
            break

    # 从下往上找第一行包含 B 的行，并记录该行中最后一个 B 的列号
    for i in range(n - 1, -1, -1):
        flag = False
        for j in range(m - 1, -1, -1):
            if li[i][j] == "B":
                flag = True
                position4 = j
                break
        if flag:
            break

    avg1 = (position1 + position2) // 2 + 1
    avg2 = (position3 + position4) // 2 + 1
    print(avg1, avg2)

if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)