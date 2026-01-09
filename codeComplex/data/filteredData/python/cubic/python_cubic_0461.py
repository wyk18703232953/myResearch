def main(n):
    # Map n to grid size and step parameter deterministically
    # Here: n controls both dimensions and k
    # n >= 2 to make vertical edges meaningful; ensure at least 2x2
    if n < 2:
        n = 2
    rows = n
    cols = n
    # Choose k proportional to n, at least 2
    k = 2 * (n // 2)
    if k == 0:
        k = 2

    # Deterministic construction of hor and ver cost grids
    # hor: rows x (cols-1)
    hor = [
        [(i + j + 1) for j in range(cols - 1)]
        for i in range(rows)
    ]
    # ver: (rows-1) x cols
    ver = [
        [(i * 2 + j + 1) for j in range(cols)]
        for i in range(rows - 1)
    ]

    # Core algorithm (unchanged logic)
    if k % 2:
        for _ in range(rows):
            # print(*([-1] * cols))
            pass
        return

    k = k // 2
    dp = [[[0] * cols for _ in range(rows)] for _ in range(k + 1)]

    for x in range(1, k + 1):
        for y in range(rows):
            for z in range(cols):
                hold = float('inf')
                if y != 0:
                    hold = min(hold, dp[x - 1][y - 1][z] + ver[y - 1][z])
                if y != rows - 1:
                    hold = min(hold, dp[x - 1][y + 1][z] + ver[y][z])
                if z != 0:
                    hold = min(hold, dp[x - 1][y][z - 1] + hor[y][z - 1])
                if z != cols - 1:
                    hold = min(hold, dp[x - 1][y][z + 1] + hor[y][z])
                dp[x][y][z] = hold

    for row in dp[k]:
        # print(*map(lambda i: i * 2, row))
        pass
if __name__ == "__main__":
    # Example fixed-size run for complexity experiments
    main(10)