def main(n):
    import random

    # 生成规模为 n 的随机测试数据
    # 这里令网格为 n 行 n 列，随机生成 '*' 或 '.'
    m = n
    a = [None] * n
    l = [None] * n
    r = [None] * n
    s = [0] * n
    res = []

    # 随机生成网格
    for i in range(n):
        row = []
        for _ in range(m):
            # 0.5 概率为 '*'，否则为 '.'
            row.append('*' if random.random() < 0.5 else '.')
        a[i] = row
        l[i] = [i for i in range(m)]
        r[i] = [i for i in range(m)]
        s[i] = [0] * m

    # 原逻辑：按行标记连续的 '*' 段
    for i in range(n):
        j = 0
        b = a[i]
        ll = l[i]
        rr = r[i]
        while j < m:
            if b[j] == '*':
                jj = j + 1
                while jj < m and b[jj] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    ll[k] = j
                    rr[k] = jj
                j = jj + 1
            else:
                j += 1

    # 原逻辑：按列计算每个中心的最大十字臂长
    for i in range(m):
        j = 0
        while j < n:
            if a[j][i] == '*':
                jj = j + 1
                while jj < n and a[jj][i] == '*':
                    jj += 1
                jj -= 1
                for k in range(j, jj + 1):
                    x = min(i - l[k][i], r[k][i] - i, k - j, jj - k)
                    s[k][i] = x
                    if x > 0:
                        res.append((k + 1, i + 1, x))
                j = jj + 1
            else:
                j += 1

    # 原逻辑：利用 s 重建出行方向的覆盖图到 r[i]
    for i in range(n):
        j = 0
        ss = s[i]
        rr = r[i]
        c = -1
        while j < m:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            else:
                rr[j] = '.'
            j += 1
            c -= 1
        j = m - 1
        c = -1
        while j >= 0:
            if ss[j] > 0 and c < ss[j]:
                c = ss[j]
            if c >= 0:
                rr[j] = '*'
            c -= 1
            j -= 1

    # 原逻辑：利用 s 重建出列方向的覆盖图到 r[j][i]，并与原图 a 对比
    for i in range(m):
        j = 0
        c = -1
        while j < n:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            j += 1
            c -= 1
        j = n - 1
        c = -1
        while j >= 0:
            x = s[j][i]
            if x > 0 and c < x:
                c = x
            if c >= 0:
                r[j][i] = '*'
            if r[j][i] != a[j][i]:
                print(-1)
                return
            c -= 1
            j -= 1

    # 输出结果
    print(len(res))
    for item in res:
        print(*item)