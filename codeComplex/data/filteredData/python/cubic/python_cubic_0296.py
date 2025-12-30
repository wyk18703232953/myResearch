import random

def main(n):
    # 1. 生成测试数据规模：将 n 平均分给 R, G, B
    #   确保每个至少为 1（当 n >= 3 时）
    if n < 3:
        # 最小情况下强制 R=G=B=1
        R = G = B = 1
    else:
        base = n // 3
        rem = n % 3
        R = base + (1 if rem > 0 else 0)
        G = base + (1 if rem > 1 else 0)
        B = base

    # 2. 生成三种颜色的数组，数值为 1..100 的随机正整数
    r = sorted([random.randint(1, 100) for _ in range(R)], reverse=True)
    g = sorted([random.randint(1, 100) for _ in range(G)], reverse=True)
    b = sorted([random.randint(1, 100) for _ in range(B)], reverse=True)

    # 3. 按原逻辑进行三维 DP 计算
    ans = 0
    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]
    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                if i < R and j < G:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + r[i] * g[j]
                    )
                if j < G and k < B:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + g[j] * b[k]
                    )
                if i < R and k < B:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + r[i] * b[k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可修改
    main(9)