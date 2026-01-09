def main(n):
    # Interpret n as the common size of the three color arrays.
    # Ensure non-negative integer size.
    r = g = b = max(0, int(n))

    # Deterministically generate R, G, B and sort them (same as original code behavior).
    # Use simple arithmetic sequences to satisfy determinism.
    R = sorted([i + 1 for i in range(r)])
    G = sorted([2 * (i + 1) for i in range(g)])
    B = sorted([3 * (i + 1) for i in range(b)])

    # DP array: dimensions (r+1) x (g+1) x (b+1)
    dp = [[[0] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i + j + k < 2:
                    continue
                val = dp[i][j][k]
                if i > 0 and j > 0:
                    val = max(val, dp[i - 1][j - 1][k] + R[i - 1] * G[j - 1])
                if i > 0 and k > 0:
                    val = max(val, dp[i - 1][j][k - 1] + R[i - 1] * B[k - 1])
                if j > 0 and k > 0:
                    val = max(val, dp[i][j - 1][k - 1] + G[j - 1] * B[k - 1])
                dp[i][j][k] = val

    return dp[r][g][b]


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments.
    result = main(5)
    # print(result)
    pass