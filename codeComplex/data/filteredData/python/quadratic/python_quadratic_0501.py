import random

def main(n):
    # 随机构造一个 n x n 的网格作为测试数据
    # 你也可以按需要改成固定模式或可重复的伪随机数据
    m = n
    A = []
    ct = []

    for _ in range(n):
        # 每个位置以 50% 概率是 '#'，否则是 '.'
        row = ['#' if random.random() < 0.5 else '.' for _ in range(m)]
        A.append(row)
        ct.append([0] * m)

    # 原逻辑：寻找特定的 3x3 形状，将其覆盖到 ct 中
    for i in range(n - 2):
        for j in range(m - 2):
            if (
                A[i][j] == '#' and
                A[i][j+1] == '#' and
                A[i][j+2] == '#' and
                A[i+1][j] == '#' and
                A[i+2][j] == '#' and
                A[i+2][j+1] == '#' and
                A[i+2][j+2] == '#' and
                A[i+1][j+2] == '#'
            ):
                ct[i][j] = 1
                ct[i][j+1] = 1
                ct[i][j+2] = 1
                ct[i+1][j] = 1
                ct[i+1][j+2] = 1
                ct[i+2][j] = 1
                ct[i+2][j+1] = 1
                ct[i+2][j+2] = 1

    xct = 0
    xhs = 0

    for i in range(n):
        for j in range(m):
            if ct[i][j] == 1:
                xct += 1
            if A[i][j] == '#':
                xhs += 1

    if xhs == xct:
        print('YES')
    else:
        print('NO')