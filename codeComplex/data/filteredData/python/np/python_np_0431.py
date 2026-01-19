def get_ans(x, a, n, m):
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
        for j in range(lim):
            if (i | j) == match and track[i] != -1 and track[j] != -1:
                return track[i], track[j]

    return -1, -1


def main(n):
    # 映射规模：n 为矩阵的行数，列数固定为 m=5
    m = 5
    if n <= 0:
        return

    # 确定性生成矩阵 a，a[i][j] 的大小大致随 i、j 增大
    # a[i][j] = i * (j + 1) + (i ^ j)
    a = [[i * (j + 1) + (i ^ j) for j in range(m)] for i in range(n)]

    lo = 0
    hi = 1000000000
    while lo < hi - 1:
        mid = (lo + hi) // 2
        i, j = get_ans(mid, a, n, m)
        if i == -1:
            hi = mid - 1
        else:
            lo = mid

    i, j = get_ans(hi, a, n, m)
    if i != -1:
        print("{} {}".format(i + 1, j + 1))
    else:
        i, j = get_ans(lo, a, n, m)
        print("{} {}".format(i + 1, j + 1))


if __name__ == "__main__":
    main(10)