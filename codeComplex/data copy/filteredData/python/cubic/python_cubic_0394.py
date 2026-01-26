def main(n):
    from math import inf

    # Scale parameters from n
    # Grid size: n x n
    # k (steps*2): proportional to n, must be even in original logic
    rows = max(1, n)
    cols = max(1, n)
    k = 2 * max(1, n // 2)  # ensure even and >=2 for n>=2

    # Deterministic construction of h (rows x (cols-1)) and v ((rows-1) x cols)
    h = []
    for i in range(rows):
        row = []
        for j in range(cols - 1):
            row.append((i + 1) + (j + 2))  # simple positive weights
        h.append(row)

    v = []
    for i in range(rows - 1):
        row = []
        for j in range(cols):
            row.append((i + 2) * (j + 1))  # simple positive weights
        v.append(row)

    # Core logic from original program
    if k & 1:
        # In original solution, print -1 grid and exit
        for i in range(rows):
            # print(*([-1] * cols))
            pass
        return

    half_k = k // 2
    dp = [[[inf] * cols for _ in range(rows)] for _ in range(half_k + 1)]
    for i in range(rows):
        for j in range(cols):
            dp[0][i][j] = 0

    for step in range(1, half_k + 1):
        for i in range(rows):
            for j in range(cols):
                cur = dp[step][i][j]
                # move up
                if i:
                    val = dp[step - 1][i - 1][j] + 2 * v[i - 1][j]
                    if val < cur:
                        cur = val
                # move down
                if i + 1 < rows:
                    val = dp[step - 1][i + 1][j] + 2 * v[i][j]
                    if val < cur:
                        cur = val
                # move left
                if j:
                    val = dp[step - 1][i][j - 1] + 2 * h[i][j - 1]
                    if val < cur:
                        cur = val
                # move right
                if j + 1 < cols:
                    val = dp[step - 1][i][j + 1] + 2 * h[i][j]
                    if val < cur:
                        cur = val
                dp[step][i][j] = cur

    for i in range(rows):
        # print(*dp[half_k][i])
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(5)