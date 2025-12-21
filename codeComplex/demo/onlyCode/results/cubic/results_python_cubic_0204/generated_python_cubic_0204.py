def func(n1, n2, n3):
    global r, g, b, dp
    if (n1 < 0 and n2 < 0) or (n3 < 0 and n2 < 0) or (n1 < 0 and n3 < 0):
        return 0
    if n1 < 0:
        return g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1)
    if n2 < 0:
        return r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1)
    if n3 < 0:
        return g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3)
    if dp[n1][n2][n3] == -1:
        dp[n1][n2][n3] = max(
            g[n2] * b[n3] + func(n1, n2 - 1, n3 - 1),
            r[n1] * b[n3] + func(n1 - 1, n2, n3 - 1),
            g[n2] * r[n1] + func(n1 - 1, n2 - 1, n3),
        )
    return dp[n1][n2][n3]


def main(n):
    global r, g, b, dp
    R = G = B = n
    r = list(range(1, R + 1))
    g = list(range(1, G + 1))
    b = list(range(1, B + 1))
    r = sorted(r)
    g = sorted(g)
    b = sorted(b)
    dp = [[[-1 for _ in range(B)] for _ in range(G)] for _ in range(R)]
    return func(R - 1, G - 1, B - 1)


if __name__ == "__main__":
    print(main(3))