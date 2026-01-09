def main(n):
    # Interpret n as the length of each of the three arrays
    r = n
    g = n
    b = n

    # Deterministic data generation
    ar = [i * 2 + 1 for i in range(r)]
    ag = [i * 3 + 2 for i in range(g)]
    ab = [i * 5 + 3 for i in range(b)]

    # Sort in descending order to match original behavior
    ar.sort(reverse=True)
    ag.sort(reverse=True)
    ab.sort(reverse=True)

    # DP memoization table
    mem = [[[-1 for _ in range(b + 1)] for _ in range(g + 1)] for _ in range(r + 1)]

    def dp(r1, g1, b1):
        if mem[r1][g1][b1] != -1:
            return mem[r1][g1][b1]

        v1, v2, v3 = 0, 0, 0

        if r1 < r:
            if g1 < g:
                v1 = (ar[r1] * ag[g1]) + dp(r1 + 1, g1 + 1, b1)
            if b1 < b:
                v2 = (ar[r1] * ab[b1]) + dp(r1 + 1, g1, b1 + 1)

        if g1 < g and b1 < b:
            v3 = (ag[g1] * ab[b1]) + dp(r1, g1 + 1, b1 + 1)

        mem[r1][g1][b1] = max(v1, v2, v3)
        return mem[r1][g1][b1]

    result = dp(0, 0, 0)
    # print(result)
    pass
    return result


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(5)