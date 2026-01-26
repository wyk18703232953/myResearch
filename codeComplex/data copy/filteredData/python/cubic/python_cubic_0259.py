def main(n):
    # Interpret n as the common size for r, g, b
    if n < 1:
        n = 1
    r = g = b = n

    # Deterministic generation of lists
    ls_r = sorted([(i * 2 + 1) % 1000 for i in range(r)])
    ls_g = sorted([(i * 3 + 2) % 1000 for i in range(g)])
    ls_b = sorted([(i * 5 + 3) % 1000 for i in range(b)])

    dp = [[[0 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    if r > 0 and g > 0:
        dp[1][1][0] = ls_r[0] * ls_g[0]
    if g > 0 and b > 0:
        dp[0][1][1] = ls_g[0] * ls_b[0]
    if r > 0 and b > 0:
        dp[1][0][1] = ls_r[0] * ls_b[0]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                res1 = 0
                res2 = 0
                res3 = 0
                if i - 1 >= 0 and j - 1 >= 0 and dp[i - 1][j - 1][k] is not None:
                    res1 = dp[i - 1][j - 1][k] + (ls_r[i - 1] * ls_g[j - 1] if i > 0 and j > 0 else 0)
                if i - 1 >= 0 and k - 1 >= 0 and dp[i - 1][j][k - 1] is not None:
                    res2 = dp[i - 1][j][k - 1] + (ls_r[i - 1] * ls_b[k - 1] if i > 0 and k > 0 else 0)
                if j - 1 >= 0 and k - 1 >= 0 and dp[i][j - 1][k - 1] is not None:
                    res3 = dp[i][j - 1][k - 1] + (ls_g[j - 1] * ls_b[k - 1] if j > 0 and k > 0 else 0)
                dp[i][j][k] = max(res1, res2, res3)

    result = dp[r][g][b]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(3)