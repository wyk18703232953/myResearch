def main(n):
    # n is the size of the probability matrix (n x n)
    if n <= 1:
        # For n <= 1, the original logic is not well-defined (division by zero in move),
        # so we handle it specially by outputting 1.000000 for the single element,
        # or nothing for n == 0.
        if n == 1:
            print("1.000000")
        else:
            print()
        return

    # Deterministically generate an n x n probability matrix `prob`
    # Example construction: prob[i][j] = ((i + 1) * (j + 2)) / (n + 3)
    prob = [
        [((i + 1) * (j + 2)) / (n + 3) for j in range(n)]
        for i in range(n)
    ]

    dp = [-1.0] * (1 << n)
    ans = [0.0] * n

    def move(mask, die):
        total = bin(mask).count('1')
        z = 0.0
        for i in range(n):
            if mask & (1 << i):
                z += prob[i][die]
        return z / ((total * (total - 1)) >> 1)

    def solve(mask):
        if mask == (1 << n) - 1:
            return 1.0
        if dp[mask] != -1.0:
            return dp[mask]
        res = 0.0
        for i in range(n):
            if not (mask & (1 << i)):
                prev = solve(mask ^ (1 << i))
                res += prev * move(mask ^ (1 << i), i)
        dp[mask] = res
        return res

    for i in range(n):
        ans[i] = "%.6f" % solve(1 << i)

    print(*ans)


if __name__ == "__main__":
    # Example deterministic call for testing / time complexity experiments
    main(4)