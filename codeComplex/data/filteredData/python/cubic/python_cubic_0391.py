def main(n):
    # Map n to grid size and k
    # For scalability and determinism:
    # n >= 2: grid size n x n, k = 2 * n (even)
    # n == 1: minimal valid grid 2 x 2, k = 2
    if n <= 1:
        rows = 2
        cols = 2
        k = 2

    else:
        rows = n
        cols = n
        k = 2 * n

    # Deterministically generate reb1 (rows x (cols - 1)) and reb2 ((rows - 1) x cols)
    # reb1[i][j] is the cost between (i,j) and (i,j+1)
    # reb2[i][j] is the cost between (i,j) and (i+1,j)
    reb1 = [[(i + 1) * (j + 2) for j in range(cols - 1)] for i in range(rows)]
    reb2 = [[(i + 2) * (j + 1) for j in range(cols)] for i in range(rows - 1)]

    # If k is odd (should not happen with the mapping above), output -1 grid
    if k % 2:
        for i in range(rows):
            for j in range(cols):
                # print(-1, end=" ")
                pass
            # print()
            pass
        return

    minsum = [[0] * cols for _ in range(rows)]
    nminsum = [[0] * cols for _ in range(rows)]

    for _ in range(k // 2):
        for i in range(rows):
            for j in range(cols):
                cmin = 1000000000010
                if i != 0:
                    cmin = min(cmin, minsum[i - 1][j] + reb2[i - 1][j])
                if i != rows - 1:
                    cmin = min(cmin, minsum[i + 1][j] + reb2[i][j])
                if j != 0:
                    cmin = min(cmin, minsum[i][j - 1] + reb1[i][j - 1])
                if j != cols - 1:
                    cmin = min(cmin, minsum[i][j + 1] + reb1[i][j])
                nminsum[i][j] = cmin
        for i in range(rows):
            for j in range(cols):
                minsum[i][j] = nminsum[i][j]

    for row in minsum:
        for val in row:
            # print(val * 2, end=" ")
            pass
        # print()
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)