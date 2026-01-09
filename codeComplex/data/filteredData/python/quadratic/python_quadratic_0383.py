def main(n):
    # Interpret n as grid size: n x n
    rows = n
    cols = n

    # Deterministic grid generation:
    # Pattern: cells on main diagonal -> 'B', others -> 'W'
    # This preserves possibility of having a center depending on n
    a = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if i == j:
                row_chars.append("B")

            else:
                row_chars.append("W")
        a.append("".join(row_chars))

    def is_center(a, y, x, n, m):
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

    # Run the original core logic
    for y in range(rows):
        found = False
        for x in range(cols):
            if is_center(a, y, x, rows, cols):
                # print(y + 1, x + 1)
                pass
                found = True
                break
        if found:
            break


if __name__ == "__main__":
    # Example deterministic call; adjust n for scaling experiments
    main(10)