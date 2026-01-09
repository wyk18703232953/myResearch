def main(n):
    # Map n to grid size: create approximately square grid
    # Ensure minimum size 3x3 to make the algorithm meaningful
    m = max(3, n)
    cols = max(3, n)

    # Deterministically generate a grid of '.' and '#'
    # Pattern: '#' when (i*j + i + j) % 3 == 0, else '.'
    l = []
    for i in range(m):
        row_chars = []
        for j in range(cols):
            if (i * j + i + j) % 3 == 0:
                row_chars.append('#')

            else:
                row_chars.append('.')
        l.append(''.join(row_chars))

    inks = []
    for i in range(1, m - 1):
        for j in range(1, cols - 1):
            if (
                l[i - 1][j - 1] == '#'
                and l[i][j - 1] == '#'
                and l[i + 1][j - 1] == '#'
                and l[i - 1][j] == '#'
                and l[i + 1][j] == '#'
                and l[i - 1][j + 1] == '#'
                and l[i][j + 1] == '#'
                and l[i + 1][j + 1] == '#'
            ):
                inks += [
                    (i - 1, j - 1),
                    (i, j - 1),
                    (i + 1, j - 1),
                    (i - 1, j),
                    (i + 1, j),
                    (i - 1, j + 1),
                    (i, j + 1),
                    (i + 1, j + 1),
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