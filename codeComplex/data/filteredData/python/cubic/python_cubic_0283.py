def main(n):
    # Map n to sizes of the three arrays; keep them balanced
    r = n
    g = n
    b = n

    # Deterministic data generation for arrays a[0], a[1], a[2]
    # Using simple arithmetic formulas to ensure reproducibility
    a = [[], [], []]
    a[0] = sorted([(i * 2 + 1) for i in range(r)])
    a[1] = sorted([(i * 3 + 2) for i in range(g)])
    a[2] = sorted([(i * 5 + 3) for i in range(b)])

    # Core DP logic unchanged, only driven by generated data
    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    odp = 0
    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < r and k < b:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < g and k < b:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > odp:
                    odp = dp[i][j][k]
    # print(odp)
    pass
if __name__ == "__main__":
    # Example call for time complexity experiments
    main(5)