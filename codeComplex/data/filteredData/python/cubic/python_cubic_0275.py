def main(n):
    # 1. 根据规模 n 生成 r, g, b
    # 这里简单设定为 r = g = b = n
    r = g = b = n

    # 2. 生成测试数据：R, G, B
    # 示例：使用等差序列，也可改为其他生成方式
    R = [i for i in range(1, r + 1)]
    G = [i for i in range(1, g + 1)]
    B = [i for i in range(1, b + 1)]

    # 排序（保持与原始代码逻辑一致）
    R.sort()
    G.sort()
    B.sort()

    # 3D 动态规划
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i and j:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1])
                if j and k:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1])
                if k and i:
                    dp[i][j][k] = max(dp[i][j][k],
                                      dp[i - 1][j][k - 1] + B[k - 1] * R[i - 1])

    # 按原代码逻辑输出结果
    print(dp[r][g][b])


if __name__ == "__main__":
    # 示例：调用 main(3)
    main(3)