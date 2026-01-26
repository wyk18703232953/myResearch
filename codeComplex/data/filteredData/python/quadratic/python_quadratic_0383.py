def is_center(a, n, m, y, x):
    count1 = count2 = count3 = count4 = 0

    # up
    y1 = y
    x1 = x
    while True:
        y2 = y1 - 1
        if y2 < 0:
            break
        c = a[y2][x]
        if c == "W":
            break
        count1 += 1
        y1 = y2

    # down
    y1 = y
    x1 = x
    while True:
        y2 = y1 + 1
        if y2 == n:
            break
        c = a[y2][x]
        if c == "W":
            break
        count2 += 1
        y1 = y2

    # left
    y1 = y
    x1 = x
    while True:
        x2 = x1 - 1
        if x2 < 0:
            break
        c = a[y1][x2]
        if c == "W":
            break
        count3 += 1
        x1 = x2

    # right
    y1 = y
    x1 = x
    while True:
        x2 = x1 + 1
        if x2 == m:
            break
        c = a[y1][x2]
        if c == "W":
            break
        count4 += 1
        x1 = x2

    return count1 == count2 == count3 == count4 and a[y][x] == "B"


def generate_grid(n):
    # Use n as both rows and columns: n x n grid
    size = n
    if size <= 0:
        return [], 0, 0

    # Construct a deterministic pattern of 'B' and 'W'
    # Pattern: cell (i,j) is 'B' if (i + j) % 3 != 0, else 'W'
    grid = []
    for i in range(size):
        row_chars = []
        for j in range(size):
            if (i + j) % 3 == 0:
                row_chars.append("W")

            else:
                row_chars.append("B")
        grid.append("".join(row_chars))
    return grid, size, size


def main(n):
    a, rows, cols = generate_grid(n)
    if rows == 0 or cols == 0:
        return None

    result = None
    for y in range(rows):
        found = False
        for x in range(cols):
            if is_center(a, rows, cols, y, x):
                result = (y + 1, x + 1)
                # print(y + 1, x + 1)
                pass
                found = True
                break
        if found:
            break
    return result


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(10)