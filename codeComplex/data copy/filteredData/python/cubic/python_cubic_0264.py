def main(n):
    # Map n to sizes of the three arrays; keep them <= 200 to respect dp size 202
    max_size = 200
    R = min(n, max_size)
    G = min(n, max_size)
    B = min(n, max_size)

    # Deterministic data generation
    r = [(i * 2 + 1) for i in range(R)]
    g = [(i * 3 + 2) for i in range(G)]
    b = [(i * 5 + 3) for i in range(B)]

    r.sort()
    g.sort()
    b.sort()

    # dp dimension is fixed 202x202x202 as in original code
    dp = [[[0] * 202 for _ in range(202)] for _ in range(202)]

    for i in range(R + 1):
        for j in range(G + 1):
            for k in range(B + 1):
                val = dp[i][j][k]
                if i and j:
                    tmp = dp[i - 1][j - 1][k] + r[i - 1] * g[j - 1]
                    if tmp > val:
                        val = tmp
                if i and k:
                    tmp = dp[i - 1][j][k - 1] + r[i - 1] * b[k - 1]
                    if tmp > val:
                        val = tmp
                if j and k:
                    tmp = dp[i][j - 1][k - 1] + g[j - 1] * b[k - 1]
                    if tmp > val:
                        val = tmp
                dp[i][j][k] = val

    # Return the final result instead of printing, so the caller can decide
    return dp[R][G][B]


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    # print(result)
    pass