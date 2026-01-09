def main(n):
    # Interpret n as both the number of rows and columns
    rows = n
    cols = n

    # Deterministically generate a rows x cols grid of '.' with a centered 'B' block.
    # Make the 'B' block size depend on n, but always valid.
    # Let block size k = max(1, n // 3).
    k = max(1, n // 3)
    # Center of the matrix (1-based indices)
    center_row = (rows + 1) // 2
    center_col = (cols + 1) // 2
    # Top-left corner of the block (1-based)
    top_row = max(1, center_row - (k - 1) // 2)
    left_col = max(1, center_col - (k - 1) // 2)
    # Bottom-right corner (1-based)
    bottom_row = min(rows, top_row + k - 1)
    right_col = min(cols, left_col + k - 1)

    x1 = -1
    x2 = -1
    y1 = -1
    y2 = -1

    for i in range(rows):
        # Build each row string deterministically
        row_chars = []
        for j in range(cols):
            # Convert to 1-based for comparison
            r = i + 1
            c = j + 1
            if top_row <= r <= bottom_row and left_col <= c <= right_col:
                row_chars.append('B')

            else:
                row_chars.append('.')
        s = ''.join(row_chars)

        for j in range(cols):
            if s[j] == 'B':
                if x1 == -1:
                    x1 = j + 1
                x2 = max(x2, j + 1)
                if y1 == -1:
                    y1 = i + 1
                y2 = i + 1

    # print((y1 + y2) // 2, (x1 + x2) // 2)
    pass
if __name__ == "__main__":
    main(10)