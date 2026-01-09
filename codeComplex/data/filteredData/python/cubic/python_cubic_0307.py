def main(n):
    # Map n to sizes of the three lists (r, g, b)
    # Use simple deterministic splits
    r = n
    g = n // 2 + 1
    b = n // 3 + 1

    # Deterministically generate lists and sort in descending order
    rl = sorted([(i * 2 + 1) for i in range(1, r + 1)], reverse=True)
    gl = sorted([(i * 3 + 2) for i in range(1, g + 1)], reverse=True)
    bl = sorted([(i * 5 + 3) for i in range(1, b + 1)], reverse=True)

    dp_table = [[[-1] * (b + 1) for _ in range(g + 1)] for _ in range(r + 1)]

    def solve(i, j, k):
        if dp_table[i][j][k] != -1:
            return dp_table[i][j][k]

        if i < r and j < g and k < b:
            m = max(
                solve(i + 1, j + 1, k) + (rl[i] * gl[j]),
                solve(i + 1, j, k + 1) + (rl[i] * bl[k]),
                solve(i, j + 1, k + 1) + (gl[j] * bl[k]),
            )
            dp_table[i][j][k] = m
            return m

        elif i < r and j < g:
            m = solve(i + 1, j + 1, b) + rl[i] * gl[j]
            dp_table[i][j][k] = m
            return m

        elif i < r and k < b:
            m = solve(i + 1, g, k + 1) + (rl[i] * bl[k])
            dp_table[i][j][k] = m
            return m

        elif j < g and k < b:
            m = solve(r, j + 1, k + 1) + (gl[j] * bl[k])
            dp_table[i][j][k] = m
            return m

        else:
            return 0

    return solve(0, 0, 0)


if __name__ == "__main__":
    # Example deterministic call
    # print(main(5))
    pass