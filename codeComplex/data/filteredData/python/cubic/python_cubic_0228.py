def main(n):
    # Map n to sizes of the three arrays
    # Ensure minimum size 1 for each dimension
    x = max(1, n)
    y = max(1, n // 2 if n >= 2 else 1)
    z = max(1, n // 3 if n >= 3 else 1)

    # Deterministic array generation based only on n and indices
    arr_x = [(i * 2 + 1) % (n + 7) + 1 for i in range(x)]
    arr_y = [(i * 3 + 2) % (n + 11) + 1 for i in range(y)]
    arr_z = [(i * 5 + 3) % (n + 13) + 1 for i in range(z)]

    # Adjust sizes as in original code
    X = x + 1
    Y = y + 1
    Z = z + 1

    lengths = [X, Y, Z]
    arrs = [arr_x, arr_y, arr_z]

    for a in arrs:
        a.sort()

    dp = [[[0 for _k in range(Z)] for _j in range(Y)] for _i in range(X)]

    for i in range(1, X):
        for j in range(1, Y):
            dp[i][j][0] = dp[i - 1][j - 1][0] + arr_x[i - 1] * arr_y[j - 1]

    for j in range(1, Y):
        for k in range(1, Z):
            dp[0][j][k] = dp[0][j - 1][k - 1] + arr_y[j - 1] * arr_z[k - 1]

    for i in range(1, X):
        for k in range(1, Z):
            dp[i][0][k] = dp[i - 1][0][k - 1] + arr_x[i - 1] * arr_z[k - 1]

    for i in range(1, X):
        for j in range(1, Y):
            for k in range(1, Z):
                opt1 = dp[i - 1][j - 1][k] + arr_x[i - 1] * arr_y[j - 1]
                opt2 = dp[i][j - 1][k - 1] + arr_y[j - 1] * arr_z[k - 1]
                opt3 = dp[i - 1][j][k - 1] + arr_x[i - 1] * arr_z[k - 1]
                dp[i][j][k] = max(opt1, opt2, opt3)

    ans = dp[X - 1][Y - 1][Z - 1]
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    # Example deterministic call for timing/complexity experiments
    main(10)