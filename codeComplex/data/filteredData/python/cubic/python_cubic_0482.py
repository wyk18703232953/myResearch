def main(n):
    # Interpret n as a grid size parameter
    # Set grid to n x n and K proportional to n (even)
    rows = n
    cols = n
    K = 2 * max(1, n // 2)  # ensure K is even and >=2

    R = rows
    C = cols

    wh = [[0] * C for _ in range(R)]
    wv = [[0] * C for _ in range(R)]

    # Deterministic generation of horizontal edge weights:
    # wh[i][j] corresponds to the original input where j ranges to m-1
    for i in range(R):
        for j in range(C - 1):
            wh[i][j] = (i + 1) + (j + 1)

    # Deterministic generation of vertical edge weights:
    # wv[i][j] corresponds to the original input where i ranges to n-1
    for i in range(R - 1):
        for j in range(C):
            wv[i][j] = (i + 1) * (j + 1)

    max_k = K // 2
    INF = int(1e8)

    f = [[[INF] * 11 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            f[i][j][0] = 0

    for k in range(1, max_k + 1):
        for i in range(R):
            for j in range(C):
                if i > 0:
                    val = f[i - 1][j][k - 1] + wv[i - 1][j]
                    if val < f[i][j][k]:
                        f[i][j][k] = val
                if j < C - 1:
                    val = f[i][j + 1][k - 1] + wh[i][j]
                    if val < f[i][j][k]:
                        f[i][j][k] = val
                if i < R - 1:
                    val = f[i + 1][j][k - 1] + wv[i][j]
                    if val < f[i][j][k]:
                        f[i][j][k] = val
                if j > 0:
                    val = f[i][j - 1][k - 1] + wh[i][j - 1]
                    if val < f[i][j][k]:
                        f[i][j][k] = val

    results = []
    for i in range(R):
        row_res = []
        for j in range(C):
            if K % 2 == 1:
                row_res.append(-1)

            else:
                dp = [INF] * (max_k + 1)
                dp[0] = 0
                for k in range(1, max_k + 1):
                    best = dp[k]
                    for l in range(0, k):
                        val = dp[l] + f[i][j][k - l] * 2
                        if val < best:
                            best = val
                    dp[k] = best
                row_res.append(dp[max_k])
        results.append(row_res)

    # For timing experiments, printing can be disabled or adjusted as needed.
    # Here we print in the same structure as the original (one per line).
    for i in range(R):
        for j in range(C):
            # print(results[i][j], end=' ')
            pass
        # print()
        pass
if __name__ == "__main__":
    main(10)