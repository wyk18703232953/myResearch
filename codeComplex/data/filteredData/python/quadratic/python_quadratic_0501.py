def main(n):
    # 定义网格规模：n 作为行数，列数与行数相同，保证 m >= 3
    if n < 3:
        n = 3
    m = n

    # 确定性生成网格 A，字符为 '#' 或 '.'：
    # 规则：若 (i * m + j) % 3 == 0 则为 '#', 否则为 '.'
    A = []
    ct = []
    for i in range(n):
        row = []
        mark_row = [0] * m
        for j in range(m):
            if (i * m + j) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        A.append(row)
        ct.append(mark_row)

    for i in range(n - 2):
        for j in range(m - 2):
            if (
                A[i][j] == '#' and A[i][j + 1] == '#' and A[i][j + 2] == '#' and
                A[i + 1][j] == '#' and A[i + 2][j] == '#' and A[i + 2][j + 1] == '#' and
                A[i + 2][j + 2] == '#' and A[i + 1][j + 2] == '#'
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