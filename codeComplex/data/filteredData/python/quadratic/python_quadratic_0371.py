import random

def main(n):
    # 生成一个 n 行 n 列的随机网格，字符为 '.' 或 '*'
    # 你可以按需要修改生成策略
    m = n
    # 至少保证有一些 '*'
    grid = []
    for _ in range(n):
        row_chars = []
        for _ in range(m):
            # 随机生成星号或点，星号概率可调
            row_chars.append('*' if random.random() < 0.4 else '.')
        grid.append(''.join(row_chars))

    # 原始逻辑开始
    row = [[[] for _ in range(m)] for _ in range(n)]
    col = [[[] for _ in range(m)] for _ in range(n)]
    visr, out, all_cnt = [[-1 for _ in range(m)] for _ in range(n)], [], 0
    visc = [[-1 for _ in range(m)] for _ in range(n)]

    # 预处理每行连续 '*' 区间
    for i in range(n):
        be, en = -1, -1
        for j in range(m):
            if grid[i][j] == '*':
                en += 1
                if be == -1:
                    be = en = j
            else:
                if be != -1:
                    for k in range(be, en + 1):
                        row[i][k] = [be, en]
                be = -1

        if be != -1:
            for k in range(be, en + 1):
                row[i][k] = [be, en]

    # 预处理每列连续 '*' 区间
    for i in range(m):
        be, en = -1, -1
        for j in range(n):
            if grid[j][i] == '*':
                en += 1
                if be == -1:
                    be = en = j
            else:
                if be != -1:
                    for k in range(be, en + 1):
                        col[k][i] = [be, en]
                be = -1

        if be != -1:
            for k in range(be, en + 1):
                col[k][i] = [be, en]

    # 枚举中心，记录能形成的“十字”
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                all_cnt += 1
                hor = min(row[i][j][1] - j, j - row[i][j][0])
                ver = min(col[i][j][1] - i, i - col[i][j][0])
                if hor <= ver:
                    ver = hor
                else:
                    hor = ver

                if hor > 0 and ver > 0:
                    out.append('%d %d %d' % (i + 1, j + 1, hor))
                    visr[i][j - ver] = j + ver
                    visc[i - hor][j] = i + hor

    dis = set()
    # 按行覆盖
    for i in range(n):
        j, ma = 0, -1
        while j < m:
            ma = max(ma, visr[i][j])
            if ma >= j:
                dis.add((i, j))
            j += 1

    # 按列覆盖
    for i in range(m):
        j, ma = 0, -1
        while j < n:
            ma = max(ma, visc[j][i])
            if ma >= j:
                dis.add((j, i))
            j += 1

    if len(dis) != all_cnt:
        print(-1)
    else:
        print('%d\n%s' % (len(out), '\n'.join(out)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)