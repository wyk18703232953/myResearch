import random


def main(n: int):
    # 1. 用 n 生成规模参数 R, G, B（可根据需要调整策略）
    #   这里简单设定三种颜色的数量都为 n
    R = G = B = n

    # 2. 生成测试数据：长度为 R/G/B 的浮点数组
    #   这里使用 [0, 1) 区间的随机浮点数
    r_sticks = sorted([random.random() for _ in range(R)], reverse=True) + [0.0]
    g_sticks = sorted([random.random() for _ in range(G)], reverse=True) + [0.0]
    b_sticks = sorted([random.random() for _ in range(B)], reverse=True) + [0.0]

    # 3. 原逻辑：三维 DP
    dp = [[[0.0] * (B + 2) for _ in range(G + 2)] for _ in range(R + 2)]

    for ri in range(R + 1):
        for gi in range(G + 1):
            for bi in range(B + 1):
                v = dp[ri][gi][bi]
                # 匹配 R-G
                dp[ri + 1][gi + 1][bi] = max(dp[ri + 1][gi + 1][bi], v + r_sticks[ri] * g_sticks[gi])
                # 匹配 R-B
                dp[ri + 1][gi][bi + 1] = max(dp[ri + 1][gi][bi + 1], v + r_sticks[ri] * b_sticks[bi])
                # 匹配 G-B
                dp[ri][gi + 1][bi + 1] = max(dp[ri][gi + 1][bi + 1], v + g_sticks[gi] * b_sticks[bi])

    ans = max(
        max(
            max(dp[r][g][b] for b in range(B + 1))
            for g in range(G + 1)
        )
        for r in range(R + 1)
    )
    print(int(ans + 1e-6))


if __name__ == '__main__':
    # 示例：使用 n = 3 运行
    main(3)