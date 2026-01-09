def main(n):
    # Interpret n as number of rows; fix m deterministically as n
    m = n

    # Deterministically generate grid with exactly one row containing 'B's
    # Place a block of consecutive 'B's in row k = n//2 (if exists) and center it
    grid = []
    b_row = n // 2 if n > 0 else 0
    b_len = max(1, m // 3) if m > 0 else 0
    if b_len > m:
        b_len = m

    if m > 0 and b_len > 0:
        start = (m - b_len) // 2

    else:
        start = 0

    for i in range(n):
        if i == b_row and m > 0 and b_len > 0:
            row = ['W'] * m
            for j in range(start, start + b_len):
                row[j] = 'B'
            grid.append(''.join(row))

        else:
            grid.append('W' * m)

    # Core logic from original program
    for i in range(n):
        mt = grid[i]
        if mt.count('B') != 0:
            # print(mt.count('B') // 2 + i + 1, mt.count('B') // 2 + mt.index('B') + 1)
            pass
            break


if __name__ == "__main__":
    main(10)