def main(n):
    # Interpret n as the length m of the array a
    m = max(1, n)

    # Deterministically generate input array a of length m
    # Example pattern: a[i] cycles through 1..5
    a = [(i % 5) + 1 for i in range(m)]

    dp = [[505] * m for _ in range(m)]
    Max = [[0] * m for _ in range(m)]

    for i in range(m):
        dp[i][i] = 1
        Max[i][i] = a[i]

    for length in range(1, m + 1):
        for i in range(m - length + 1):
            j = i + length - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                if dp[i][k] == 1 and dp[k + 1][j] == 1 and Max[i][k] == Max[k + 1][j]:
                    dp[i][j] = 1
                    Max[i][j] = Max[i][k] + 1

    # For experimental use, return the result instead of printing only
    return dp[0][m - 1]


if __name__ == "__main__":
    # Example fixed-size run for reproducibility
    result = main(10)
    # print(result)
    pass