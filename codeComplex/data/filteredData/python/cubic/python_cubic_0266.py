def main(n):
    # Interpret n as the common size of the three color arrays
    r = g = b = max(1, n)

    # Deterministic data generation based on n and indices
    R = [i * 2 + 1 for i in range(1, r + 1)]
    G = [i * 3 + 2 for i in range(1, g + 1)]
    B = [i * 5 + 3 for i in range(1, b + 1)]

    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]
    R.sort(reverse=True)
    G.sort(reverse=True)
    B.sort(reverse=True)
    R.insert(0, 0)
    G.insert(0, 0)
    B.insert(0, 0)
    dp[0][0][0], ans = 0, 0
    for i in range(0, r + 1):
        for j in range(0, g + 1):
            for k in range(0, b + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                if i and j and dp[i - 1][j - 1][k] != -1:
                    val = dp[i - 1][j - 1][k] + R[i] * G[j]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if k and j and dp[i][j - 1][k - 1] != -1:
                    val = dp[i][j - 1][k - 1] + B[k] * G[j]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if i and k and dp[i - 1][j][k - 1] != -1:
                    val = dp[i - 1][j][k - 1] + R[i] * B[k]
                    if val > dp[i][j][k]:
                        dp[i][j][k] = val
                if dp[i][j][k] > ans:
                    ans = dp[i][j][k]
    # print(ans)
    pass
if __name__ == "__main__":
    main(3)