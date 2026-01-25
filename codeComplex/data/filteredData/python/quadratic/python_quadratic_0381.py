def main(n):
    # Interpret n as both number of rows and columns
    rows = n
    cols = n
    if rows <= 0 or cols <= 0:
        return

    # Deterministically construct grid s with exactly one contiguous segment of 'B'
    # Place the segment on row mid_row, from mid_col to mid_col + seg_len - 1
    mid_row = rows // 2
    seg_len = max(1, cols // 3)
    mid_col = max(0, (cols - seg_len) // 2)

    s = []
    for i in range(rows):
        if i == mid_row:
            row_chars = []
            for j in range(cols):
                if mid_col <= j < mid_col + seg_len:
                    row_chars.append('B')
                else:
                    row_chars.append('.')
            s.append("".join(row_chars))
        else:
            s.append("." * cols)

    # Original algorithm logic
    for i in range(rows):
        for j in range(cols):
            if s[i][j] == 'B':
                cnt = 1
                for k in range(j + 1, cols):
                    if s[i][k] == 'B':
                        cnt += 1
                    else:
                        break
                print(i + 1 + cnt // 2, j + 1 + cnt // 2)
                return


if __name__ == "__main__":
    main(10)