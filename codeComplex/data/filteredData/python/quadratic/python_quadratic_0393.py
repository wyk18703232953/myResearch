def main(n):
    # Interpreting n as both number of rows and columns in a square grid
    rows = n
    cols = n

    # Deterministic grid generation:
    # Create a single horizontal segment of 'B's in the middle row.
    # Segment length is n if n is odd, else n-1 to keep it within bounds and non-empty.
    grid = []
    mid_row = rows // 2
    seg_len = n if n % 2 == 1 else max(1, n - 1)
    start_col = (cols - seg_len) // 2

    for i in range(rows):
        if i == mid_row:
            row_chars = []
            for j in range(cols):
                if start_col <= j < start_col + seg_len:
                    row_chars.append('B')

                else:
                    row_chars.append('.')
            grid.append("".join(row_chars))

        else:
            grid.append("." * cols)

    # Original algorithm logic
    lock = 0
    Ccen = 0
    Rcen = 0
    for i in range(rows):
        s = str(grid[i])
        if ('B' in s) and (lock == 0):
            Rstart = s.index('B')
            cnt = s.count('B')
            Rcen = Rstart + (cnt // 2)
            Cstart = i
            Ccen = Cstart + (cnt // 2)
            lock = 1

    # print(Ccen + 1, Rcen + 1)
    pass
if __name__ == "__main__":
    main(5)