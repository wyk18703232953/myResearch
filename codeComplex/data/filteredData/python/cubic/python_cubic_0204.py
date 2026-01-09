def func(n1, n2, n3, r, g, b, dp):
    if (n1 < 0 and n2 < 0) or (n3 < 0 and n2 < 0) or (n1 < 0 and n3 < 0):
        return 0
    if n1 < 0:
        return g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1, r, g, b, dp)
    if n2 < 0:
        return r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1, r, g, b, dp)
    if n3 < 0:
        return g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3, r, g, b, dp)
    if dp[n1][n2][n3] == -1:
        dp[n1][n2][n3] = max(
            g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1, r, g, b, dp),
            r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1, r, g, b, dp),
            g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3, r, g, b, dp),
        )
    return dp[n1][n2][n3]


def main(n):
    # Interpret n as total size, split into three arrays of sizes:
    # R = n, G = n, B = n  (cubic DP in n)
    if n <= 0:
        return 0

    R = n
    G = n
    B = n

    # Deterministic generation of arrays r, g, b
    r = [i + 1 for i in range(R)]
    g = [2 * (i + 1) for i in range(G)]
    b = [3 * (i + 1) for i in range(B)]

    r = sorted(r)
    g = sorted(g)
    b = sorted(b)

    dp = [[[-1 for _ in range(B)] for _ in range(G)] for _ in range(R)]

    result = func(R - 1, G - 1, B - 1, r, g, b, dp)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(3)