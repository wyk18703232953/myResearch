def main(n):
    INF = 10**9
    # Deterministic generation of input array a based on n
    # Example: a[i] = (i % 5) + 1 to keep values small but structured
    a = [(i % 5) + 1 for i in range(n)]

    dp = [[INF] * (n + 1) for _ in range(n + 1)]
    val = [[-1] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        dp[i][i + 1] = 1
        val[i][i + 1] = a[i]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l
            for k in range(i + 1, j):
                if dp[i][k] == 1 and dp[k][j] == 1 and val[i][k] == val[k][j]:
                    dp[i][j] = 1
                    val[i][j] = val[i][k] + 1

                else:
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    # print(dp[0][n])
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)