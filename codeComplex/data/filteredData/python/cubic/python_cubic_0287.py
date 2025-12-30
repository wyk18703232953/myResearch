import random

def main(n: int) -> int:
    """
    n 为规模参数，这里用来控制 R, G, B 的大小以及生成数据的范围。
    返回最大面积 area。
    """
    # 根据 n 生成 R, G, B，可按需调整策略
    # 这里简单设置为不超过 n 的随机正整数，且至少为 1
    R = random.randint(1, n)
    G = random.randint(1, n)
    B = random.randint(1, n)

    # 生成测试数据：长度分别为 R, G, B 的随机正整数序列
    # 数值范围也与 n 相关，可按需调整
    r = [random.randint(1, n) for _ in range(R)]
    g = [random.randint(1, n) for _ in range(G)]
    b = [random.randint(1, n) for _ in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    # 三维 DP，dp[i][j][k] 表示 r 取前 i 个，g 取前 j 个，b 取前 k 个时的最大值
    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    area = 0
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1])
                if j > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1])
                if i > 0 and k > 0:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1])
                if dp[i][j][k] > area:
                    area = dp[i][j][k]

    print(area)
    return area


if __name__ == "__main__":
    # 示例：用 n=10 运行一次
    main(10)