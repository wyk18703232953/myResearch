import random

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
    # 生成测试数据：
    # n 行，m 列的矩阵 a，元素为 [0, 1e9] 之间的随机整数
    # 为保证位掩码复杂度可控，这里固定 m 较小（例如 8）
    m = 8
    MAX_VAL = 10**9

    a = [[random.randint(0, MAX_VAL) for _ in range(m)] for _ in range(n)]

    lo = 0
    hi = MAX_VAL
    while lo < hi - 1:
        mid = (lo + hi) // 2
        i, j = get_ans(mid, a, n, m)
        if i == -1:
            hi = mid - 1
        else:
            lo = mid

    i, j = get_ans(hi, a, n, m)
    if i != -1:
        print(i + 1, j + 1)
    else:
        i, j = get_ans(lo, a, n, m)
        print(i + 1, j + 1)


# 示例调用：
# main(10)