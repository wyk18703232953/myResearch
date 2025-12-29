def main(n):
    import random

    # 1. 生成测试数据
    # 生成长度为 n 的数组 a，元素为 0..(2^20-1) 间的随机整数
    a = [random.randint(0, (1 << 20) - 1) for _ in range(n)]

    # 生成查询数 q 和 q 个区间 [l, r]（1-based，且 l <= r）
    # 这里令 q = n，区间随机生成
    q = n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2. 原逻辑：构建 f 和 dp
    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        f[i][i] = dp[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # 3. 输出：先输出生成的数据，后输出每个查询的答案
    # 便于调试和复用
    print(n)
    print(" ".join(map(str, a)))
    print(q)
    for l, r in queries:
        print(l, r)
    for l, r in queries:
        print(dp[l - 1][r - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)