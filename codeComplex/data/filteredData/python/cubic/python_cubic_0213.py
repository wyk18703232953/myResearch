import random

def main(n: int):
    # 生成规模：r, g, b 之和约为 n，尽量均分
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # 生成测试数据：正整数，范围可自行调整
    R = [random.randint(1, 1000) for _ in range(r)]
    G = [random.randint(1, 1000) for _ in range(g)]
    B = [random.randint(1, 1000) for _ in range(b)]

    R.sort()
    G.sort()
    B.sort()

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    dp[i + 1][j + 1][k] = max(
                        dp[i + 1][j + 1][k],
                        dp[i][j][k] + R[i] * G[j]
                    )
                if i < r and k < b:
                    dp[i + 1][j][k + 1] = max(
                        dp[i + 1][j][k + 1],
                        dp[i][j][k] + R[i] * B[k]
                    )
                if j < g and k < b:
                    dp[i][j + 1][k + 1] = max(
                        dp[i][j + 1][k + 1],
                        dp[i][j][k] + G[j] * B[k]
                    )

    print(dp[r][g][b])

if __name__ == "__main__":
    # 示例：可以在此修改 n 的值进行测试
    main(9)