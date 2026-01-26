def main(n):
    # Map n to grid size: create an n x n grid
    if n < 3:
        n = 3
    rows = n
    cols = n

    MAP = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if (i // 2 + j // 3) % 2 == 0:
                row.append("#")

            else:
                row.append(".")
        MAP.append(row)

    ANSMAP = [["." for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (
                MAP[i - 1][j - 1] == "#"
                and MAP[i - 1][j] == "#"
                and MAP[i - 1][j + 1] == "#"
                and MAP[i][j - 1] == "#"
                and MAP[i][j + 1] == "#"
                and MAP[i + 1][j - 1] == "#"
                and MAP[i + 1][j] == "#"
                and MAP[i + 1][j + 1] == "#"
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
    main(10)