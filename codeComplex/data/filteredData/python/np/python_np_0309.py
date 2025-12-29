mod = 998244353

def main(n):
    # 生成规模为 n 的测试数据：
    # 令 N = n，K = max(1, n // 2) 作为一个与 n 同阶的参数
    N = n
    K = max(1, n // 2)

    dp = [[[0] * (K + 2) for _ in range(2)] for _ in range(N)]
    dp[0][0][0] = 1
    dp[0][1][1] = 1

    for i in range(1, N):
        for b in range(K):
            dp[i][0][b]   += dp[i - 1][0][b]
            dp[i][0][b]   += dp[i - 1][1][b]
            dp[i][0][b]   += dp[i - 1][1][b]
            dp[i][0][b + 1] += dp[i - 1][0][b]
            dp[i][0][b]   %= mod

            dp[i][1][b + 1] += dp[i - 1][0][b]
            dp[i][1][b]     += dp[i - 1][1][b]
            dp[i][1][b + 2] += dp[i - 1][1][b]
            dp[i][1][b + 1] += dp[i - 1][0][b]
            dp[i][1][b]     %= mod

    ans = 0
    for x in range(2):
        ans += dp[N - 1][x][K - 1]

    ans = ans * 2 % mod
    print(ans)
    return ans

if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)