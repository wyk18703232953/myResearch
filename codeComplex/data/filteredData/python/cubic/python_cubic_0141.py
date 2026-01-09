def main(n):
    # Deterministically generate input of size n
    # Original input:
    # n
    # a[0..n-1]
    a = [i % 5 + 1 for i in range(n)]

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = a[i]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n, 1):
            for k in range(i, j, 1):
                if dp[i][k] and dp[i][k] == dp[k + 1][j]:
                    dp[i][j] = dp[i][k] + 1
    b = [10 ** 10] * (n + 1)
    b[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j][i - 1]:
                b[i] = min(b[i], b[j] + 1)
    # print(b[n])
    pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)