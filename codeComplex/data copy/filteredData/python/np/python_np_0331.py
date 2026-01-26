ch_0 = {0: [0, 1, 2], 2: [2], 1: [1], 3: [1, 2, 3]}
ch_1 = {0: [3], 3: [0], 1: [0, 3], 2: [0, 3]}
ch_2 = {0: [], 3: [], 2: [1], 1: [2]}
MOD = 998244353


def solve(n, k):
    dp = [[[0] * 4 for _ in range(k + 5)] for _ in range(n + 5)]
    dp[0][1][3] = 1
    dp[0][1][0] = 1
    dp[0][2][1] = 1
    dp[0][2][2] = 1

    for i in range(1, n):
        for j in range(1, k + 1):
            for mask in range(4):
                for t in ch_0[mask]:
                    dp[i][j][mask] = (dp[i][j][mask] + dp[i - 1][j][t]) % MOD
                if j > 1:
                    for t in ch_1[mask]:
                        dp[i][j][mask] = (dp[i][j][mask] + dp[i - 1][j - 1][t]) % MOD
                    if j > 2:
                        for t in ch_2[mask]:
                            dp[i][j][mask] = (dp[i][j][mask] + dp[i - 1][j - 2][t]) % MOD

    ans = 0
    for mask in range(4):
        ans = (ans + dp[n - 1][k][mask]) % MOD
    return ans


def main(n):
    # 根据规模 n 生成测试数据，这里令 k 与 n 相同
    k = n
    result = solve(n, k)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)