def main(n):
    # Map n to sizes of the three arrays; keep them balanced for scaling
    # Ensure at least size 1 for each dimension
    r = max(1, n // 3)
    g = max(1, (n - r) // 2)
    b = max(1, n - r - g)

    # Deterministic generation of arrays, then sort in descending order
    ra = sorted([(i * 2 + 1) for i in range(r)], reverse=True)
    ga = sorted([(i * 3 + 2) for i in range(g)], reverse=True)
    ba = sorted([(i * 5 + 3) for i in range(b)], reverse=True)

    # Initialize DP array with -1
    dp = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(i, j, k):
        if dp[i][j][k] != -1:
            return dp[i][j][k]

        if i == r:
            if j == g or k == b:
                return 0
            dp[i][j][k] = ga[j] * ba[k] + solve(i, j + 1, k + 1)

        elif j == g:
            if i == r or k == b:
                return 0
            dp[i][j][k] = ra[i] * ba[k] + solve(i + 1, j, k + 1)

        elif k == b:
            if j == g or i == r:
                return 0
            dp[i][j][k] = ga[j] * ra[i] + solve(i + 1, j + 1, k)

        else:
            dp[i][j][k] = max(
                ra[i] * ga[j] + solve(i + 1, j + 1, k),
                ra[i] * ba[k] + solve(i + 1, j, k + 1),
                ba[k] * ga[j] + solve(i, j + 1, k + 1),
            )

        return dp[i][j][k]

    result = solve(0, 0, 0)
    # print(result)
    pass
if __name__ == "__main__":
    main(30)