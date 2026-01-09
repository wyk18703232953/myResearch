def main(n):
    # Map n to sizes of the three arrays
    R = max(1, n)
    G = max(1, n)
    B = max(1, n)

    # Deterministically generate arrays r, g, b
    r = [(i * 2 + 1) % 1000 for i in range(R)]
    g = [(i * 3 + 2) % 1000 for i in range(G)]
    b = [(i * 5 + 3) % 1000 for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    dp = [[[0 for _ in range(B + 1)] for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            dp[i][j][0] = dp[i - 1][j - 1][0] + r[i - 1] * g[j - 1]

    for j in range(1, G + 1):
        for k in range(1, B + 1):
            dp[0][j][k] = dp[0][j - 1][k - 1] + b[k - 1] * g[j - 1]

    for i in range(1, R + 1):
        for k in range(1, B + 1):
            dp[i][0][k] = dp[i - 1][0][k - 1] + r[i - 1] * b[k - 1]

    for i in range(1, R + 1):
        for j in range(1, G + 1):
            for k in range(1, B + 1):
                ri = r[i - 1]
                gj = g[j - 1]
                bk = b[k - 1]
                m = ri
                if gj > m:
                    m = gj
                if bk > m:
                    m = bk
                if m == ri:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + ri * gj,
                        dp[i - 1][j][k - 1] + ri * bk,
                    )
                elif m == gj:
                    dp[i][j][k] = max(
                        dp[i - 1][j - 1][k] + ri * gj,
                        dp[i][j - 1][k - 1] + gj * bk,
                    )

                else:
                    dp[i][j][k] = max(
                        dp[i][j - 1][k - 1] + bk * gj,
                        dp[i - 1][j][k - 1] + ri * bk,
                    )

    result = dp[R][G][B]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)