import random

def main(n):
    # 根据 n 构造一个 n 行 n 列的随机棋盘，'*' 和 '.' 随机分布
    m = n
    c = []
    for _ in range(n):
        row = [random.choice(['*', '.']) for _ in range(m)]
        c.append(row)

    a = []
    e = []
    g = []

    # 差分数组初始化
    for _ in range(n):
        e.append([0] * m)
    for _ in range(n):
        g.append([0] * m)

    # 方向 DP 数组初始化
    dpu = [[0] * m for _ in range(n)]
    dpd = [[0] * m for _ in range(n)]
    dpl = [[0] * m for _ in range(n)]
    dpr = [[0] * m for _ in range(n)]

    # 向上、向左
    for i in range(n):
        for j in range(m):
            if c[i][j] == "*":
                if i > 0:
                    dpu[i][j] = dpu[i - 1][j] + 1
                else:
                    dpu[i][j] = 1
                if j > 0:
                    dpl[i][j] = dpl[i][j - 1] + 1
                else:
                    dpl[i][j] = 1

    # 向下、向右
    i = n - 1
    while i >= 0:
        j = m - 1
        while j >= 0:
            if c[i][j] == "*":
                if i < n - 1:
                    dpd[i][j] = dpd[i + 1][j] + 1
                else:
                    dpd[i][j] = 1
                if j < m - 1:
                    dpr[i][j] = dpr[i][j + 1] + 1
                else:
                    dpr[i][j] = 1
            j -= 1
        i -= 1

    # 找到所有十字中心及其臂长
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if c[i][j] == "*":
                k = min(
                    dpd[i][j] - 1,
                    dpu[i][j] - 1,
                    dpr[i][j] - 1,
                    dpl[i][j] - 1,
                )
                if k > 0:
                    a.append([i + 1, j + 1, k])
                    # 纵向差分
                    e[i - k][j] += 1
                    if i + k < n - 1:
                        e[i + k + 1][j] -= 1
                    # 横向差分
                    g[i][j - k] += 1
                    if j + k < m - 1:
                        g[i][j + k + 1] -= 1

    # 纵向前缀和
    for col in range(m):
        for row in range(1, n):
            if c[row - 1][col] == "*":
                e[row][col] += e[row - 1][col]

    # 横向前缀和
    for row in range(n):
        for col in range(1, m):
            if c[row][col - 1] == "*":
                g[row][col] += g[row][col - 1]

    # 检查是否所有 '*' 都被覆盖
    f = 0
    for i in range(n):
        for j in range(m):
            if c[i][j] == "*" and e[i][j] <= 0 and g[i][j] <= 0:
                f = 1
                break
        if f == 1:
            break

    if f == 1:
        print(-1)
    else:
        print(len(a))
        for triple in a:
            print(*triple)