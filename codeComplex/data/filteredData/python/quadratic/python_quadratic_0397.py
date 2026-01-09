def main(n):
    # Interpret n as both number of rows and columns for scalability
    rows = n
    cols = n

    # Deterministically construct the grid M with '0'
    M = [['0' for _ in range(cols)] for _ in range(rows)]

    # Deterministically place a contiguous block of 'B's forming a square or rectangle
    # For determinism and scalability:
    # - side length (or dimension) is max(1, n // 3)
    # - top-left corner is (start_row, start_col) chosen so that the block fits inside the grid
    if rows > 0 and cols > 0:
        side = max(1, n // 3)
        side = min(side, rows, cols)
        start_row = rows // 4
        start_col = cols // 3
        if start_row + side > rows:
            start_row = max(0, rows - side)
        if start_col + side > cols:
            start_col = max(0, cols - side)

        for r in range(start_row, start_row + side):
            for c in range(start_col, start_col + side):
                M[r][c] = 'B'

    start = []
    end = []
    for a in range(rows):
        for b in range(cols):
            if M[a][b] == 'B':
                if not start:
                    start.append(a + 1)
                    start.append(b + 1)

                else:
                    end.clear()
                    end.append(a + 1)
                    end.append(b + 1)

    if not start or not end:
        # print(start[0], start[1])
        pass

    else:
        mid1 = int((end[0] + start[0]) / 2)
        mid2 = int((end[1] + start[1]) / 2)
        # print(mid1, mid2)
        pass
if __name__ == "__main__":
    main(10)