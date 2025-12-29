import random

def main(n: int):
    # 1. 根据规模 n 生成三种颜色数组长度
    # 控制总状态数量 (c1+1)*(c2+1)*(c3+1) 约为 O(n^3)，避免过大
    c1 = max(1, n)
    c2 = max(1, n)
    c3 = max(1, n)

    # 2. 生成测试数据：整数数组 r, g, b
    # 数值范围可根据需要调整
    r = sorted(random.randint(1, 10**4) for _ in range(c1))
    g = sorted(random.randint(1, 10**4) for _ in range(c2))
    b = sorted(random.randint(1, 10**4) for _ in range(c3))

    # 3. 原始 DP 逻辑
    dp = [[[0 for _ in range(c3 + 1)] for _ in range(c2 + 1)] for _ in range(c1 + 1)]

    for i in range(c1 + 1):
        for j in range(c2 + 1):
            for k in range(c3 + 1):
                if i > 0 and j > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    )
                if i > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    )
                if j > 0 and k > 0:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    )

    # 4. 输出最终结果
    print(dp[c1][c2][c3])


if __name__ == "__main__":
    # 示例：n = 30，可根据需要调整
    main(30)