def main(n):
    # 为了保证可规模化，这里将 n 视为原问题中区间数量
    # m 设为 2*n + 1，保证所有 w[i] < m
    m = 2 * n + 1

    # 生成严格递增的 w，长度为 n
    # 这里简单生成奇数序列：1, 3, 5, ..., 2*n-1
    w = [2 * i + 1 for i in range(n)]

    # 保持原始逻辑
    w = [0] + w + [m]
    c, d = [], []
    res = 0
    for j in range(n + 1):
        c.append(res)
        if j % 2 == 0:
            res += w[j + 1] - w[j]
    res = 0
    for j in range(n + 1, -1, -1):
        if j % 2 == 0 and j != n + 1:
            res += w[j + 1] - w[j]
        d.append(res)
    d = d[::-1]
    mx = d[0]
    for j in range(n + 1):
        mx = max(c[j] + (w[j + 1] - w[j] - 1) + (m - w[j + 1] - d[j + 1]), mx)
    print(mx)


if __name__ == "__main__":
    main(5)