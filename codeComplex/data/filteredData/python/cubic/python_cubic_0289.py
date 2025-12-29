import random

def main(n: int):
    # 生成规模：r, g, b 都约为 n
    r = g = b = n

    # 生成测试数据：颜色值在 1~10^4 范围内
    R = [random.randint(1, 10_000) for _ in range(r)]
    G = [random.randint(1, 10_000) for _ in range(g)]
    B = [random.randint(1, 10_000) for _ in range(b)]

    # 以下为原逻辑
    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    R.insert(0, 0)
    G.insert(0, 0)
    B.insert(0, 0)
    dp[0][0][0], ans = 0, 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i and j and dp[i - 1][j - 1][k] != -1:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j - 1][k] + R[i] * G[j]
                    )
                if k and j and dp[i][j - 1][k - 1] != -1:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i][j - 1][k - 1] + B[k] * G[j]
                    )
                if i and k and dp[i - 1][j][k - 1] != -1:
                    dp[i][j][k] = max(
                        dp[i][j][k],
                        dp[i - 1][j][k - 1] + R[i] * B[k]
                    )
                ans = max(ans, dp[i][j][k])

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)