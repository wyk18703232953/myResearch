def main(n):
    # Generate deterministic 4 boards of size n x n with digits 0/1 based on simple arithmetic
    a = []
    for i in range(4):
        board = []
        for y in range(n):
            row = []
            for x in range(n):
                # Example deterministic pattern: depend on i, x, y
                val = (i + x + 2 * y) % 2
                row.append(val)
            board.append(row)
        a.append(board)

    # Original logic using generated a
    b = []
    for i in range(4):
        b.append([])
        for j in range(2):
            c = 0
            for y in range(n):
                for x in range(n):
                    if j == 1:
                        z = (x + y) % 2

                    else:
                        z = 1 - (x + y) % 2
                    c += a[i][y][x] != z
            b[-1].append(c)
    ans = float("inf")
    for i in (3, 5, 6, 9, 10, 12):
        ans = min(
            ans,
            b[0][i & 1]
            + b[1][i >> 1 & 1]
            + b[2][i >> 2 & 1]
            + b[3][i >> 3 & 1],
        )
    # print(ans)
    pass
    return ans


if __name__ == "__main__":
    main(5)