#!/usr/bin/env python3

import random

def main(n: int):
    # 1. 生成测试数据
    # 生成长度为 n 的数组 a，元素为 0~10^9 的随机整数
    a = [random.randint(0, 10**9) for _ in range(n)]

    # 生成查询数量 q（这里设为 n，按需要可调整）
    q = n
    # 随机生成 q 个区间 [l, r]，1 <= l <= r <= n
    queries = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        queries.append((l, r))

    # 2. 按原逻辑计算 f 和 dp
    dp = [[0] * n for _ in range(n)]
    f = [[0] * n for _ in range(n)]

    # 计算 f[i][j]：从下往上构建 XOR-pyramid
    for i in range(n - 1, -1, -1):
        f[i][i] = a[i]
        for j in range(i + 1, n):
            f[i][j] = f[i][j - 1] ^ f[i + 1][j]

    # 计算 dp[i][j]：区间 [i, j] 上 f 的最大值
    for i in range(n - 1, -1, -1):
        dp[i][i] = f[i][i]
        for j in range(i + 1, n):
            dp[i][j] = max(f[i][j], dp[i][j - 1], dp[i + 1][j])

    # 3. 输出内容（可按需求调整，这里保持与原程序查询行为一致）
    # 先输出用于调试的测试数据与结果，可根据需要删减
    print("n =", n)
    print("a =", a)
    print("q =", q)
    print("queries =", queries)
    print("answers:")

    for l, r in queries:
        print(dp[l - 1][r - 1])


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)