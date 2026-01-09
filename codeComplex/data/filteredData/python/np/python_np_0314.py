def main(n: int):
    MOD = 998244353

    # 生成测试数据：将原先的输入 n, K 中的 K 由 n 推出
    # 可根据需要调整生成方式，这里示例设为 K = min(n, 10)
    K = min(n, 10)

    dp = [[[0] * 4 for _ in range(K + 2)] for _ in range(n)]
    dp[0][1][0] = 1
    dp[0][1][1] = 1
    dp[0][2][2] = 1
    dp[0][2][3] = 1

    for i in range(n - 1):
        for j in range(1, K + 1):
            if j < K + 1:
                for k in range(4):
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD

                for k in range(2):
                    dp[i + 1][j][k] += dp[i][j][2]
                    dp[i + 1][j][k] %= MOD

                for k in range(2):
                    dp[i + 1][j][k] += dp[i][j][3]
                    dp[i + 1][j][k] %= MOD

        for j in range(1, K):
            for k in range(4):
                if k != 0:
                    dp[i + 1][j + 1][k] += dp[i][j][0]
                    dp[i + 1][j + 1][k] %= MOD

            for k in range(4):
                if k != 1:
                    dp[i + 1][j + 1][k] += dp[i][j][1]
                    dp[i + 1][j + 1][k] %= MOD

            if j + 2 < K + 1:
                dp[i + 1][j + 2][2] += dp[i][j][3]
                dp[i + 1][j + 2][2] %= MOD
                dp[i + 1][j + 2][3] += dp[i][j][2]
                dp[i + 1][j + 2][3] %= MOD

    num = 0
    for i in range(4):
        num += dp[n - 1][K][i]
        num %= MOD

    # print(num)
    pass
if __name__ == "__main__":
    # 示例调用：规模 n = 20
    main(20)