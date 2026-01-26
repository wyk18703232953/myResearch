def main(n):
    if n <= 0:
        return 0

    # Map n to sizes of r, g, b such that r+g+b = n (or close)
    r = n // 3
    g = (n - r) // 2
    b = n - r - g

    # Ensure non-negative sizes
    r = max(r, 0)
    g = max(g, 0)
    b = max(b, 0)

    # Deterministic construction of arrays
    ls_r = sorted([(i * 2 + 1) for i in range(r)])
    ls_g = sorted([(i * 3 + 2) for i in range(g)])
    ls_b = sorted([(i * 5 + 3) for i in range(b)])

    dp = [[[None for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def recursive(idx_r, idx_g, idx_b):
        if dp[idx_r][idx_g][idx_b] is not None:
            return dp[idx_r][idx_g][idx_b]
        res_1 = 0
        res_2 = 0
        res_3 = 0
        if (idx_r - 1) >= 0 and (idx_g - 1) >= 0:
            res_1 = recursive(idx_r - 1, idx_g - 1, idx_b) + ls_r[idx_r - 1] * ls_g[idx_g - 1]
        if (idx_g - 1) >= 0 and (idx_b - 1) >= 0:
            res_2 = recursive(idx_r, idx_g - 1, idx_b - 1) + ls_g[idx_g - 1] * ls_b[idx_b - 1]
        if (idx_r - 1) >= 0 and (idx_b - 1) >= 0:
            res_3 = recursive(idx_r - 1, idx_g, idx_b - 1) + ls_r[idx_r - 1] * ls_b[idx_b - 1]

        dp[idx_r][idx_g][idx_b] = max(res_1, res_2, res_3)
        return dp[idx_r][idx_g][idx_b]

    result = recursive(r, g, b)
    return result


if __name__ == "__main__":
    # Example deterministic calls for experimentation
    for n in [1, 3, 6, 9]:
        # print(n, main(n))
        pass