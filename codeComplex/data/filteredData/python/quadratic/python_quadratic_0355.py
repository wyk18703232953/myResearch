def main(n):
    import random
    import sys

    # 生成规模为 n 的随机测试数据（n 行 n 列）
    # 至少保证有一颗星，否则总是 -1 太无聊
    rows = []
    has_star = False
    for _ in range(n):
        row = []
        for _ in range(n):
            ch = '*' if random.random() < 0.4 else '.'
            if ch == '*':
                has_star = True
            row.append(ch)
        rows.append(''.join(row))
    if not has_star:
        # 强行放一颗星
        i = random.randrange(n)
        j = random.randrange(n)
        rows[i] = rows[i][:j] + '*' + rows[i][j+1:]

    l = rows
    n = len(l)
    m = len(l[0]) if n > 0 else 0

    # 下面是原逻辑（删除了所有 input()），直接在生成的数据上运行

    colsum = [[0 for _ in range(m)] for _ in range(n)]
    rowsum = [[0 for _ in range(m)] for _ in range(n)]
    col = [[0 for _ in range(m)] for _ in range(n)]
    row = [[0 for _ in range(m)] for _ in range(n)]
    tot = []

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                rowsum[i][j] = 1
                colsum[i][j] = 1
                row[i][j] = 1
                col[i][j] = 1

    for i in range(n):
        for j in range(1, m):
            if l[i][j] == '.':
                continue
            rowsum[i][j] += rowsum[i][j - 1]

    for i in range(n):
        for j in range(m - 2, -1, -1):
            if l[i][j] == '.':
                continue
            row[i][j] += row[i][j + 1]

    for i in range(m):
        for j in range(n - 2, -1, -1):
            if l[j][i] == '.':
                continue
            col[j][i] += col[j + 1][i]

    for i in range(m):
        for j in range(1, n):
            if l[j][i] == '.':
                continue
            colsum[j][i] += colsum[j - 1][i]

    def check(x, y):
        i = x
        j = y
        ans = min(row[i][j], rowsum[i][j], colsum[i][j], col[i][j]) - 1
        if ans == 0:
            return []
        return [ans]

    h = [[0 for _ in range(m + 1)] for _ in range(n)]
    v = [[0 for _ in range(m)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*':
                ans = check(i, j)
                for j1 in ans:
                    tot.append([i + 1, j + 1, j1])
                    h[i][j - j1] += 1
                    h[i][j + j1 + 1] -= 1
                    v[i - j1][j] += 1
                    v[i + j1 + 1][j] -= 1

    for i in range(n):
        for j in range(1, m):
            h[i][j] += h[i][j - 1]

    for i in range(m):
        for j in range(1, n):
            v[j][i] += v[j - 1][i]

    for i in range(n):
        for j in range(m):
            if l[i][j] == '*' and h[i][j] == 0 and v[i][j] == 0:
                print(-1)
                return

    print(len(tot))
    for tri in tot:
        print(*tri)