def main(n):
    # Map n to sizes of the three arrays
    # Ensure at least size 1 for each when n > 0
    a = max(1, n // 3)
    b = max(1, n // 3)
    c = max(1, n - a - b)
    # Deterministic data generation
    x = [i + 1 for i in range(a)]
    y = [2 * (i + 1) for i in range(b)]
    z = [3 * (i + 1) for i in range(c)]
    x.sort(reverse=True)
    y.sort(reverse=True)
    z.sort(reverse=True)
    ans = 0
    dp = [[[0 for _ in range(c + 2)] for _ in range(b + 2)] for _ in range(a + 1)]
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                if i < a and j < b:
                    v = dp[i][j][k] + x[i] * y[j]
                    if v > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = v
                if i < a and k < c:
                    v = dp[i][j][k] + x[i] * z[k]
                    if v > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = v
                if k < c and j < b:
                    v = dp[i][j][k] + z[k] * y[j]
                    if v > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = v
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)