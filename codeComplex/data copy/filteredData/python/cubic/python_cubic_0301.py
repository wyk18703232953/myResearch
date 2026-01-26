def main(n):
    # Interpret n as total number of elements across r, g, b
    # Split n deterministically into three parts
    n = max(1, int(n))
    nr = n // 3
    ng = (n + 1) // 3
    nb = n - nr - ng

    # Ensure each list has at least 1 element to keep the original logic meaningful
    nr = max(1, nr)
    ng = max(1, ng)
    nb = max(1, nb)

    # Deterministic data generation using simple arithmetic progressions
    r = [i * 2 + 1 for i in range(nr)]
    g = [i * 3 + 2 for i in range(ng)]
    b = [i * 5 + 4 for i in range(nb)]

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

    for i in range(max(nr, ng, nb)):
        dp(min(i, nr - 1), min(i, ng - 1), min(i, nb - 1))

    result = dp(nr - 1, ng - 1, nb - 1)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    main(10)