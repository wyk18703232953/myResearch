def main(n):
    # Interpret n as both number of rows and columns for a square grid
    # Generate a deterministic n x n MAP of '#' and '.' with a simple pattern
    MAP = []
    for i in range(n):
        row = []
        for j in range(n):
            # Example deterministic pattern: '#' if (i+j) is even, else '.'
            # This preserves enough structure for the original algorithm to run
            if (i + j) % 2 == 0:
                row.append('#')

            else:
                row.append('.')
        MAP.append(row)

    m = n  # since we used an n x n grid

    ANSMAP = [["." for _ in range(m)] for _ in range(n)]

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if (
                MAP[i - 1][j - 1] == "#" and
                MAP[i - 1][j] == "#" and
                MAP[i - 1][j + 1] == "#" and
                MAP[i][j - 1] == "#" and
                MAP[i][j + 1] == "#" and
                MAP[i + 1][j - 1] == "#" and
                MAP[i + 1][j] == "#" and
                MAP[i + 1][j + 1] == "#"
            ):
                ANSMAP[i - 1][j - 1] = "#"
                ANSMAP[i - 1][j] = "#"
                ANSMAP[i - 1][j + 1] = "#"
                ANSMAP[i][j - 1] = "#"
                ANSMAP[i][j + 1] = "#"
                ANSMAP[i + 1][j - 1] = "#"
                ANSMAP[i + 1][j] = "#"
                ANSMAP[i + 1][j + 1] = "#"

    if MAP == ANSMAP:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different scales
    main(10)