def main(n):
    # Interpret n as total length of three arrays; split deterministically
    if n < 3:
        n = 3
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # Deterministic generation of sorted arrays rr, gg, bb
    rr = [i * 2 + 1 for i in range(r)]
    gg = [i * 3 + 2 for i in range(g)]
    bb = [i * 5 + 3 for i in range(b)]

    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]
    res = 0
    for i in range(r, -1, -1):
        for j in range(g, -1, -1):
            for k in range(b, -1, -1):
                if i > 0 and j > 0:
                    dp[i - 1][j - 1][k] = max(dp[i - 1][j - 1][k], dp[i][j][k] + rr[i - 1] * gg[j - 1])
                if i > 0 and k > 0:
                    dp[i - 1][j][k - 1] = max(dp[i - 1][j][k - 1], dp[i][j][k] + rr[i - 1] * bb[k - 1])
                if j > 0 and k > 0:
                    dp[i][j - 1][k - 1] = max(dp[i][j - 1][k - 1], dp[i][j][k] + gg[j - 1] * bb[k - 1])
                if i > 0 and j > 0 and k > 0:
                    res = max(res, dp[i - 1][j - 1][k], dp[i - 1][j][k - 1], dp[i][j - 1][k - 1])
                elif i > 0 and j > 0:
                    res = max(res, dp[i - 1][j - 1][k])
                elif i > 0 and k > 0:
                    res = max(res, dp[i - 1][j][k - 1])
                elif j > 0 and k > 0:
                    res = max(res, dp[i][j - 1][k - 1])
    # print(res)
    pass
if __name__ == "__main__":
    main(30)