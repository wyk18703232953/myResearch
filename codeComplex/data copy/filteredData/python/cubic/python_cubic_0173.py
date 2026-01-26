def main(n):
    INF = 10**3
    # Deterministically generate A of length n
    A = [(i % 5) + 1 for i in range(n)]

    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    val = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = 1
        val[i][i + 1] = A[i]

    for d in range(2, n + 1):
        for i in range(n + 1 - d):
            j = i + d
            for k in range(i + 1, j):
                if dp[i][k] == 1 and dp[k][j] == 1 and val[i][k] == val[k][j]:
                    if 1 < dp[i][j]:
                        dp[i][j] = 1
                        val[i][j] = val[i][k] + 1

                else:
                    temp = dp[i][k] + dp[k][j]
                    if temp < dp[i][j]:
                        dp[i][j] = temp

    # print(dp[0][n])
    pass
if __name__ == "__main__":
    main(10)