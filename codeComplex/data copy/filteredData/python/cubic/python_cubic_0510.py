def main(n):
    # Map n to problem parameters
    # Ensure at least 1x1 grid and even k
    if n <= 0:
        n = 1
    rows = max(1, n)
    cols = max(1, n)
    k = 2 * max(1, n // 2)  # ensure k is even and roughly scales with n

    # Deterministic construction of h and v
    # h: rows x cols horizontal edge weights (except last column unused per row)
    h = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # simple deterministic weight based on indices
            row.append((i + 1) * (j + 1))
        h.append(row)

    # v: (rows - 1) x cols vertical edge weights
    v = []
    for i in range(rows - 1):
        row = []
        for j in range(cols):
            row.append((i + j + 2))
        v.append(row)

    # If k is odd (should not happen due to construction), print -1
    if k % 2:
        for i in range(rows):
            line = " ".join(str(-1) for _ in range(cols))
            # print(line)
            pass
        return

    # DP initialization
    steps = k // 2
    dp = [[[float('inf')] * cols for _ in range(rows)] for _ in range(steps + 1)]
    for i in range(rows):
        for j in range(cols):
            dp[0][i][j] = 0

    # DP transitions
    for x in range(1, steps + 1):
        for i in range(rows):
            for j in range(cols):
                best = dp[x][i][j]
                if i != 0:
                    cost = dp[x - 1][i - 1][j] + v[i - 1][j]
                    if cost < best:
                        best = cost
                if i != rows - 1:
                    cost = dp[x - 1][i + 1][j] + v[i][j]
                    if cost < best:
                        best = cost
                if j != 0:
                    cost = dp[x - 1][i][j - 1] + h[i][j - 1]
                    if cost < best:
                        best = cost
                if j != cols - 1:
                    cost = dp[x - 1][i][j + 1] + h[i][j]
                    if cost < best:
                        best = cost
                dp[x][i][j] = best

    # Output result
    for i in range(rows):
        line = " ".join(str(2 * dp[steps][i][j]) for j in range(cols))
        # print(line)
        pass
if __name__ == "__main__":
    # Example deterministic run for n = 5
    main(5)