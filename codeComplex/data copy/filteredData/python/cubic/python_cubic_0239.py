def main(n):
    # Map n to sizes of the three arrays.
    # For scalability and symmetry, split n approximately into three parts.
    a = n // 3
    b = (n + 1) // 3
    c = n - a - b
    if a == 0:
        a = 1
    if b == 0:
        b = 1
    if c == 0:
        c = 1

    # Deterministically generate arrays rs, gs, bs based on n and indices
    # Ensure positive integers and some variation
    rs = sorted([(i + 1) * 2 for i in range(a)])
    gs = sorted([(j + 1) * 3 for j in range(b)])
    bs = sorted([(k + 1) * 5 for k in range(c)])

    # Initialize dp table
    dp = [[[-1 for _ in range(c + 1)] for _ in range(b + 1)] for _ in range(a + 1)]

    def solve(i, j, k):
        if (i < 0 and j < 0) or (j < 0 and k < 0) or (i < 0 and k < 0):
            return 0
        if dp[i][j][k] != -1:
            return dp[i][j][k]
        ans = 0
        if i >= 0 and j >= 0:
            ans = max(ans, rs[i] * gs[j] + solve(i - 1, j - 1, k))
        if i >= 0 and k >= 0:
            ans = max(ans, rs[i] * bs[k] + solve(i - 1, j, k - 1))
        if j >= 0 and k >= 0:
            ans = max(ans, bs[k] * gs[j] + solve(i, j - 1, k - 1))
        dp[i][j][k] = ans
        return ans

    result = solve(a - 1, b - 1, c - 1)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(9)