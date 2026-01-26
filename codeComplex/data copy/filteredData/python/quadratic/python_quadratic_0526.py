def main(n):
    # Map n to grid size n x n
    if n < 3:
        # For very small n, no internal cells to check; just trivial grid
        n = 3
    rows = n
    cols = n

    # Deterministic generation of a '#' / '.' grid
    # Pattern: cell (i, j) is '#' if (i * 131 + j * 17) % 5 < 2 else '.'
    a = []
    array = []
    for i in range(rows):
        row_chars = []
        row_vals = []
        for j in range(cols):
            if (i * 131 + j * 17) % 5 < 2:
                row_chars.append('#')
                row_vals.append(1)

            else:
                row_chars.append('.')
                row_vals.append(0)
        a.append(row_chars)
        array.append(row_vals)

    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            f = a[y + 1][x] == '#' and a[y + 1][x + 1] == '#' and a[y + 1][x - 1] == '#'
            s = a[y][x + 1] == '#' and a[y][x - 1] == '#'
            th = a[y - 1][x] == '#' and a[y - 1][x + 1] == '#' and a[y - 1][x - 1] == '#'
            if f and s and th:
                array[y + 1][x] -= 1
                array[y + 1][x + 1] -= 1
                array[y + 1][x - 1] -= 1
                array[y][x + 1] -= 1
                array[y][x - 1] -= 1
                array[y - 1][x - 1] -= 1
                array[y - 1][x] -= 1
                array[y - 1][x + 1] -= 1

    mb = True
    for y in range(rows):
        for x in range(cols):
            if array[y][x] == 1:
                mb = False
                break
        if not mb:
            break

    if mb:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)