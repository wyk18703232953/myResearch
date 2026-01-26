def main(n):
    # 将 n 映射到原问题的规模参数
    # 这里设定：
    #   N = n            原代码中的 n
    #   K = max(1, n // 10)
    #   M = min(n, max(1, 3 * n // 4))
    N = max(1, n)
    K = max(1, n // 10)
    M = min(N, max(1, 3 * N // 4))

    # 生成一个严格递增的列表 l，长度为 M
    # 让元素分布在 [1, 2N] 区间，保持确定性
    l = []
    cur = 1
    for i in range(M):
        # 间隔在 {1, 2, 3} 中循环，用简单算术构造
        step = (i % 3) + 1
        cur += step
        l.append(cur)

    # 原核心算法逻辑（不依赖输入）
    out = 0
    d = 0

    while M > d:
        nex = l[d]
        page = (nex - d - 1) // K
        add = 1
        while d + add < M and (page * K) < l[d + add] - d <= (page + 1) * K:
            add += 1
        d += add
        out += 1

    # print(out)
    pass
if __name__ == "__main__":
    # 示例：使用 n = 100 作为规模参数
    main(100)