def main(n):
    # Interpret n as the total length of all three arrays.
    # Split deterministically into R, G, B as evenly as possible.
    if n < 0:
        n = 0
    R = n // 3
    G = (n + 1) // 3
    B = n - R - G

    # Deterministic data generation for r, g, b
    r = [i * 2 + 1 for i in range(R)]
    g = [i * 3 + 2 for i in range(G)]
    b = [i * 5 + 3 for i in range(B)]

    r.sort(reverse=True)
    g.sort(reverse=True)
    b.sort(reverse=True)

    dp = [[[0] * (B + 1) for _ in range(G + 1)] for _ in range(R + 1)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                c = False
                if i < R and j < G:
                    val = dp[i][j][k] + r[i] * g[j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                    c = True
                if j < G and k < B:
                    val = dp[i][j][k] + g[j] * b[k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                    c = True
                if k < B and i < R:
                    val = dp[i][j][k] + b[k] * r[i]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                    c = True

                if not c:
                    if i < R:
                        if dp[i][j][k] > dp[i + 1][j][k]:
                            dp[i + 1][j][k] = dp[i][j][k]
                    if j < G:
                        if dp[i][j][k] > dp[i][j + 1][k]:
                            dp[i][j + 1][k] = dp[i][j][k]
                    if k < B:
                        if dp[i][j][k] > dp[i][j][k + 1]:
                            dp[i][j][k + 1] = dp[i][j][k]

    ans = 0
    for i in dp:
        for j in i:
            mj = max(j)
            if mj > ans:
                ans = mj
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)