def main(n):
    # n controls the grid size n x n
    m = n
    listi = []
    # deterministic generation: put a block of 'B' in the middle row
    mid_row = n // 2
    block_len = max(1, n // 3)
    start_col = (n - block_len) // 2
    end_col = start_col + block_len  # exclusive

    for i in range(n):
        if i == mid_row:
            row_chars = []
            for j in range(n):
                if start_col <= j < end_col:
                    row_chars.append("B")
                else:
                    row_chars.append("W")
            listi.append("".join(row_chars))
        else:
            listi.append("W" * n)

    rownum = 0
    flag = False
    for row in listi:
        for letter in row:
            if "B" in row:
                p = row.index("B")
                s = row[::-1]
                q = abs(m - s.index("B") - 1)
                if p == q:
                    print(rownum + 1, row.index(row[p]) + 1)
                    flag = True
                    break
                mr = (q + p) / 2
                length = abs(q - p + 1)
                rn = rownum + length // 2
                print(rn + 1, int(mr + 1))
                flag = True
                break
        if flag:
            break
        rownum += 1


if __name__ == "__main__":
    main(5)