import random

def main(n):
    # 生成规模为 n 的测试数据，这里取一个接近正方形的网格
    # 你可以根据需要调整 m 和星号分布策略
    m = max(1, n)  # 简单设置为 m = n
    # 随机生成由 '*' 和 '.' 构成的 n x m 网格
    # 为了保证有一定概率存在十字形，星号密度取 0.5
    c = []
    for _ in range(n):
        row = []
        for _ in range(m):
            row.append('*' if random.random() < 0.5 else '.')
        c.append(row)

    a = []
    e = []
    g = []

    for _ in range(n):
        e.append([0] * m)
    for _ in range(n):
        g.append([0] * m)

    dpu = []
    for _ in range(n):
        dpu.append([0] * m)
    dpd = []
    for _ in range(n):
        dpd.append([0] * m)
    dpl = []
    for _ in range(n):
        dpl.append([0] * m)
    dpr = []
    for _ in range(n):
        dpr.append([0] * m)

    # 上、左方向的连续 '*' 数量
    for i in range(n):
        for j in range(m):
            if c[i][j] == "*":
                if i > 0:
                    dpu[i][j] += dpu[i - 1][j] + 1
                else:
                    dpu[i][j] = 1
                if j > 0:
                    dpl[i][j] = dpl[i][j - 1] + 1
                else:
                    dpl[i][j] = 1

    # 下、右方向的连续 '*' 数量
    i = n - 1
    while i >= 0:
        j = m - 1
        while j >= 0:
            if c[i][j] == "*":
                if i < (n - 1):
                    dpd[i][j] += dpd[i + 1][j] + 1
                else:
                    dpd[i][j] = 1
                if j < (m - 1):
                    dpr[i][j] = dpr[i][j + 1] + 1
                else:
                    dpr[i][j] = 1
            j -= 1
        i -= 1

    # 统计每个中心能形成的十字并做差分标记
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if c[i][j] == "*":
                k = min(dpd[i][j] - 1, dpu[i][j] - 1, dpr[i][j] - 1, dpl[i][j] - 1)
                if k == 0:
                    pass
                elif k > 0:
                    a.append([i + 1, j + 1, k])
                    e[i - k][j] += 1
                    if (i + k) < (n - 1):
                        e[i + k + 1][j] += -1
                    g[i][j - k] += 1
                    if (j + k) < (m - 1):
                        g[i][j + k + 1] += -1

    # 将竖向差分数组前缀和展开
    for i in range(m):
        for j in range(1, n):
            if c[j - 1][i] == "*":
                e[j][i] += e[j - 1][i]

    # 将横向差分数组前缀和展开
    for i in range(n):
        for j in range(1, m):
            if c[i][j - 1] == "*":
                g[i][j] += g[i][j - 1]

    # 检查是否存在未被任何十字覆盖的 '*'
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
        for j in a:
            print(*j)


if __name__ == "__main__":
    # 示例：可以在这里调用 main，实际评测时只需要 main(n)
    main(5)