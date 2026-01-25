def main(n):
    # 映射规模：n -> 棋盘为 n x n
    if n < 3:
        n = 3
    m = n

    # 构造确定性输入棋盘 a：按行列规则生成 '#' / '.'
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            # 简单确定性构造：根据 (i+j) 的奇偶决定字符
            if (i // 2 + j // 3) % 2 == 0:
                row.append('#')
            else:
                row.append('.')
        a.append(row)

    b = [list('.' * m) for _ in range(n)]
    start = 0

    for i in range(n):
        if start == 0 and '.' in a[i]:
            start = ((i - 3) // 3) * 3

    if start < 0:
        start = 0
    if start > n:
        start = n

    for i in range(start):
        b[i] = list('#' * m)

    for i in range(start, n - 2):
        for j in range(m - 2):
            ok = True
            if a[i][j] == '#':
                for y in range(i, i + 3):
                    if not ok:
                        break
                    for x in range(j, j + 3):
                        if not (y == i + 1 and x == j + 1):
                            if a[y][x] != '#':
                                ok = False
                                break
                if ok:
                    for y in range(i, i + 3):
                        for x in range(j, j + 3):
                            if not (y == i + 1 and x == j + 1):
                                b[y][x] = '#'

    if a == b:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main(10)