def main(n):
    # Interpret n as the maximum length for each of r, g, b lists
    # Use a simple deterministic mapping
    r = n
    g = n
    b = n

    # Deterministically generate data based on n
    # Values grow with index but are small enough for moderate n
    ls_r = sorted([(i * 2 + 1) % (2 * n + 1) for i in range(r)], reverse=False)
    ls_g = sorted([(i * 3 + 2) % (2 * n + 1) for i in range(g)], reverse=False)
    ls_b = sorted([(i * 5 + 3) % (2 * n + 1) for i in range(b)], reverse=False)

    dp = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def recursive(idx_r, idx_g, idx_b):
        if dp[idx_r][idx_g][idx_b] != -1:
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
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(3)