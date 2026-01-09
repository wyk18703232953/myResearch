def main(n):
    # Map n to sizes of r, g, b with a simple deterministic pattern
    # Make sure they don't exceed 200 because dp dimension is fixed to 201
    max_size = 200
    r = min(max(1, n), max_size)
    g = min(max(1, (2 * n) // 3 + 1), max_size)
    b = min(max(1, (n // 2) + 1), max_size)

    # Deterministic generation of rs, gs, bs using simple arithmetic patterns
    rs = [(i * 3 + 1) % 1000 for i in range(r)]
    gs = [(i * 5 + 2) % 1000 for i in range(g)]
    bs = [(i * 7 + 3) % 1000 for i in range(b)]

    rs.sort()
    gs.sort()
    bs.sort()
    rs.reverse()
    gs.reverse()
    bs.reverse()

    dp = [[[0] * 201 for _ in range(201)] for _ in range(201)]
    limit_rg = min(r, g)
    limit_gb = min(g, b)
    limit_br = min(b, r)

    for i in range(limit_rg + 1):
        for j in range(limit_gb + 1):
            for k in range(limit_br + 1):
                options = []
                if i != 0:
                    if i + k - 1 < r and i + j - 1 < g:
                        options.append(dp[i - 1][j][k] + rs[i + k - 1] * gs[i + j - 1])

                    else:
                        options.append(dp[i - 1][j][k])
                if j != 0:
                    if i + j - 1 < g and j + k - 1 < b:
                        options.append(dp[i][j - 1][k] + gs[i + j - 1] * bs[j + k - 1])

                    else:
                        options.append(dp[i][j - 1][k])
                if k != 0:
                    if j + k - 1 < b and i + k - 1 < r:
                        options.append(dp[i][j][k - 1] + bs[j + k - 1] * rs[i + k - 1])

                    else:
                        options.append(dp[i][j][k - 1])
                if options:
                    dp[i][j][k] = max(options)

    result = dp[limit_rg][limit_gb][limit_br]
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(50)