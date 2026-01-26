def main(n):
    a = [0] + [i % 5 for i in range(1, n + 1)]
    dp = [[[ -1, -1, -1 ] for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][i] = [a[i], a[i], 1]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n + 1):
            mini = 10 ** 10
            for k in range(j - i):
                x = dp[i][i + k][2] + dp[i + k + 1][j][2]
                if dp[i][i + k][1] == dp[i + k + 1][j][0]:
                    if mini > x - 1:
                        mini = x - 1
                        dp[i][j][0] = dp[i][i + k][0] + (1 if dp[i][i + k][2] == 1 else 0)
                        dp[i][j][1] = dp[i + k + 1][j][1] + (1 if dp[i + k + 1][j][2] == 1 else 0)
                        dp[i][j][2] = x - 1

                else:
                    if mini > x:
                        mini = x
                        dp[i][j][0] = dp[i][i + k][0]
                        dp[i][j][1] = dp[i + k + 1][j][1]
                        dp[i][j][2] = x
    # print(dp[1][n][2])
    pass
if __name__ == "__main__":
    main(10)