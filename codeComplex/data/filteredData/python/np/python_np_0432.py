def main(n):
    # 确定性生成 n, m 和矩阵 a
    # 这里将 m 也与 n 相关联，保证可规模化
    m = max(1, n // 2)
    if m > 15:
        m = 15  # 防止 2^m 爆炸式增长影响实验

    # 生成一个 n x m 的整数矩阵 a
    # 元素通过简单算术构造，完全确定
    a = [[(i * 131 + j * 17 + 7) % 1000000000 for j in range(m)] for i in range(n)]

    def get_ans(x):
        lim = 1 << m
        match = lim - 1
        track = [-1 for _ in range(lim)]

        for i in range(n):
            mask = 0
            for j in range(m):
                if a[i][j] >= x:
                    mask |= 1 << j
            track[mask] = i

        for i in range(lim):
            if track[i] == -1:
                continue
            for j in range(lim):
                if track[j] == -1:
                    continue
                if (i | j) == match:
                    return track[i], track[j]

        return -1, -1

    lo = 0
    hi = 1000000000
    while lo < hi - 1:
        mid = (lo + hi) // 2  # 使用整数除法
        i, j = get_ans(mid)
        if i == -1:
            hi = mid - 1
        else:
            lo = mid

    i, j = get_ans(hi)
    if i != -1:
        print("{} {}".format(i + 1, j + 1))
    else:
        i, j = get_ans(lo)
        print("{} {}".format(i + 1, j + 1))


if __name__ == "__main__":
    # 示例调用，n 为规模参数，可自行修改
    main(10)