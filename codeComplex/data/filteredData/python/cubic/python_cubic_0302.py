def main(n):
    # Interpret n as the common size of r, g, b
    nr = ng = nb = max(1, n)

    # Deterministic construction of arrays
    r = [(i * 2 + 1) % 100000 for i in range(nr)]
    g = [(i * 3 + 2) % 100000 for i in range(ng)]
    b = [(i * 5 + 3) % 100000 for i in range(nb)]

    r.sort()
    g.sort()
    b.sort()

    memo = [[[-1 for _ in range(nb + 1)] for __ in range(ng + 1)] for ___ in range(nr + 1)]
    memo[0][0][0] = 0
    for i in range(nr):
        memo[i + 1][0][0] = 0
    for j in range(ng):
        memo[0][j + 1][0] = 0
    for k in range(nb):
        memo[0][0][k + 1] = 0

    def dp(i, j, k):
        if i < -1 or j < -1 or k < -1:
            return -float("inf")
        if memo[i + 1][j + 1][k + 1] == -1:
            memo[i + 1][j + 1][k + 1] = max(
                dp(i, j - 1, k - 1) + g[j] * b[k],
                dp(i - 1, j - 1, k) + r[i] * g[j],
                dp(i - 1, j, k - 1) + r[i] * b[k],
            )
        return memo[i + 1][j + 1][k + 1]

    result = dp(nr - 1, ng - 1, nb - 1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(3)