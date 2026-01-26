from math import inf

def main(n):
    # Map n to grid size and step count deterministically
    # Ensure positive dimensions
    if n < 2:
        n_val = 2

    else:
        n_val = n
    # Choose grid as roughly sqrt-scaled, k proportional to dimension
    m = n_val
    n_rows = n_val
    k = 2 * (n_val if n_val % 2 == 0 else n_val + 1)

    # Deterministic cost generation
    horizontal_costs = [
        [(i * m + j + 1) % 7 + 1 for j in range(m - 1)]
        for i in range(n_rows)
    ]
    vertical_costs = [
        [((i + 1) * m + j + 3) % 9 + 1 for j in range(m)]
        for i in range(n_rows - 1)
    ]

    max_c = k // 2
    dp = [[[inf] * (max_c + 1) for _ in range(m)] for _ in range(n_rows)]

    def find_cost(a, b, c):
        if a < 0 or a > n_rows - 1 or b < 0 or b > m - 1:
            return inf
        if c == 0:
            return 0
        if dp[a][b][c] != inf:
            return dp[a][b][c]

        best = inf
        if a < n_rows - 1:
            val = find_cost(a + 1, b, c - 1) + vertical_costs[a][b]
            if val < best:
                best = val
        if b < m - 1:
            val = find_cost(a, b + 1, c - 1) + horizontal_costs[a][b]
            if val < best:
                best = val
        if b > 0:
            val = find_cost(a, b - 1, c - 1) + horizontal_costs[a][b - 1]
            if val < best:
                best = val
        if a > 0:
            val = find_cost(a - 1, b, c - 1) + vertical_costs[a - 1][b]
            if val < best:
                best = val

        dp[a][b][c] = best
        return best

    ans = [[inf] * m for _ in range(n_rows)]
    if k % 2 == 1:
        for i in range(n_rows):
            for j in range(m):
                ans[i][j] = -1

    else:
        half = k // 2
        for i in range(n_rows):
            for j in range(m):
                ans[i][j] = 2 * find_cost(i, j, half)

    for row in ans:
        # print(*row)
        pass
if __name__ == "__main__":
    main(10)