def main(n):
    # 映射 n 为矩阵规模：n -> n x n
    if n < 3:
        n = 3
    m = n

    # 构造确定性的棋盘格 #/. 模式
    A = []
    ct = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append('#')

            else:
                row.append('.')
        A.append(row)
        ct.append([0] * m)

    for i in range(n - 2):
        for j in range(m - 2):
            if (
                A[i][j] == '#'
                and A[i][j + 1] == '#'
                and A[i][j + 2] == '#'
                and A[i + 1][j] == '#'
                and A[i + 2][j] == '#'
                and A[i + 2][j + 1] == '#'
                and A[i + 2][j + 2] == '#'
                and A[i + 1][j + 2] == '#'
            ):
                ct[i][j] = 1
                ct[i][j + 1] = 1
                ct[i][j + 2] = 1
                ct[i + 1][j] = 1
                ct[i + 1][j + 2] = 1
                ct[i + 2][j] = 1
                ct[i + 2][j + 1] = 1
                ct[i + 2][j + 2] = 1

    xct = 0
    xhs = 0

    for i in range(len(ct)):
        for j in range(len(ct[i])):
            if ct[i][j] == 1:
                xct += 1
            if A[i][j] == '#':
                xhs += 1

    if xhs == xct:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)