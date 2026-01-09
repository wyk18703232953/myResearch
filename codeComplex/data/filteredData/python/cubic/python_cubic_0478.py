def main(n):
    # Map n to grid size and k (must be even to exercise main logic)
    # Ensure n is at least 2 to have a meaningful grid
    if n < 2:
        n_effective = 2

    else:
        n_effective = n

    # Define grid dimensions and k based on n_effective
    rows = n_effective
    cols = n_effective
    # Choose k as an even number depending on n_effective but capped for dp size (max k index 24)
    k = min(2 * (n_effective // 2 + 1), 24)
    if k % 2 == 1:
        k += 1
    if k < 2:
        k = 2

    n_val = rows
    m_val = cols

    # Deterministic generation of wh (left-right weights) of size n x (m-1)
    wh = []
    for i in range(n_val):
        row = []
        for j in range(m_val - 1):
            # Simple deterministic weight formula
            row.append((i + 1) * (j + 2) % 17 + 1)
        wh.append(row)

    # Deterministic generation of wv (top-bottom weights) of size (n-1) x m
    wv = []
    for i in range(n_val - 1):
        row = []
        for j in range(m_val):
            # Simple deterministic weight formula
            row.append((i + 2) * (j + 1) % 19 + 1)
        wv.append(row)

    # Core logic from original code, adapted to generated n_val, m_val, k, wh, wv
    if k % 2 != 0:
        ans = [[-1 for _ in range(m_val)] for _ in range(n_val)]
        for res in ans:
            # print(*res)
            pass

    else:
        # dp dimensions: i up to n_val, j up to m_val, x up to k
        # Original uses dp[505][505][25], keep that but we will only index within needed ranges
        max_n = 505
        max_m = 505
        max_k = 25
        dp = [[[0 for _ in range(max_k)] for _ in range(max_m)] for _ in range(max_n)]

        for x in range(1, k + 1):
            for i in range(1, n_val + 1):
                for j in range(1, m_val + 1):
                    dp[i][j][x] = 1234567890
                    if i != n_val:
                        dp[i][j][x] = min(
                            dp[i][j][x],
                            dp[i + 1][j][x - 1] + wv[i - 1][j - 1],
                        )
                    if i != 1:
                        dp[i][j][x] = min(
                            dp[i][j][x],
                            dp[i - 1][j][x - 1] + wv[i - 2][j - 1],
                        )
                    if j != m_val:
                        dp[i][j][x] = min(
                            dp[i][j][x],
                            dp[i][j + 1][x - 1] + wh[i - 1][j - 1],
                        )
                    if j != 1:
                        dp[i][j][x] = min(
                            dp[i][j][x],
                            dp[i][j - 1][x - 1] + wh[i - 1][j - 2],
                        )
        for i in range(1, n_val + 1):
            row_out = []
            for j in range(1, m_val + 1):
                best = 1234567890
                for x in range(1, k + 1):
                    if k % x == 0 and (k // x) % 2 == 0:
                        best = min(best, dp[i][j][x] * (k // x))
                row_out.append(str(best))
            # print(" ".join(row_out))
            pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size for experiments
    main(10)