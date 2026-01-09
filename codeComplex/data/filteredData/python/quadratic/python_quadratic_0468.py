def main(n):
    # n 表示 N 的规模
    N = n
    if N <= 0:
        return

    # 构造一个确定性的 za 数组
    # 这里使用一个简单的模式：za[i] = N - (i % k) - 1，其中 k = max(1, N//3)
    # 这样会产生重复值以及递减结构，便于覆盖算法逻辑
    k = max(1, N // 3 if N >= 3 else 1)
    za = [N - (i % k) - 1 for i in range(N)]

    # 根据 za 反推出 zl, zr，使得原算法检查能通过
    zl = [0] * N
    zr = [0] * N
    for i in range(N):
        li = 0
        ri = 0
        for j in range(i):
            if za[j] > za[i]:
                li += 1
        for j in range(i + 1, N):
            if za[j] > za[i]:
                ri += 1
        zl[i] = li
        zr[i] = ri

    # 原算法逻辑，使用构造好的 N, zl, zr
    zt = [(zl[i] + zr[i], i) for i in range(N)]
    zt.sort()
    za2 = [0 for _ in range(N)]
    now = N
    for i in range(N):
        if i > 0 and zt[i - 1][0] < zt[i][0]:
            now -= 1
        za2[zt[i][1]] = now

    # 校验
    for i in range(N):
        l = 0
        r = 0
        for j in range(i):
            if za2[j] > za2[i]:
                l += 1
        for j in range(i + 1, N):
            if za2[j] > za2[i]:
                r += 1
        if zl[i] != l or zr[i] != r:
            # print('NO')
            pass
            return

    # print('YES')
    pass
    for i in range(N):
        # print(za2[i], end=' ')
        pass
    # print()
    pass
if __name__ == "__main__":
    # 示例：使用 n=10 作为规模
    main(10)