def main(n):
    # Interpret n as the side length of a square grid
    # m = number of rows, n = number of columns in original code
    m = n
    cols = n

    # Deterministic grid generation:
    # Create a pattern with 3x3 blocks of '#' separated by '.' so that
    # the algorithm has a meaningful workload while still ending YES.
    grid = []
    for i in range(m):
        row_chars = []
        for j in range(cols):
            if 1 <= i < m - 1 and 1 <= j < cols - 1:
                # Place '#' in a 3x3 block pattern controlled by n
                if (i // 3 + j // 3) % 2 == 0:
                    row_chars.append('#')

                else:
                    row_chars.append('.')

            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))

    l = grid
    inks = []
    for i in range(1, m - 1):
        for j in range(1, cols - 1):
            if (
                l[i - 1][j - 1] == '#' and l[i][j - 1] == '#' and l[i + 1][j - 1] == '#' and
                l[i - 1][j] == '#' and l[i + 1][j] == '#' and
                l[i - 1][j + 1] == '#' and l[i][j + 1] == '#' and l[i + 1][j + 1] == '#'
            ):
                inks += [
                    (i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
                    (i - 1, j),                 (i + 1, j),
                    (i - 1, j + 1), (i, j + 1), (i + 1, j + 1),
                ]

    for i in range(m):
        for j in range(cols):
            if l[i][j] == '#' and (i, j) not in inks:
                # print("NO")
                pass
                return
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)