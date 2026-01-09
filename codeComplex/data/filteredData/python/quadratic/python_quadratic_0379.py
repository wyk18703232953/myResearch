def main(n):
    # Interpret n as the size of the square grid: n x n
    # Generate a deterministic grid with a contiguous 'B' segment in one row
    size = max(1, n)
    grid = []

    # Choose the row to contain 'B's and the start and end positions deterministically
    row_with_B = size // 2
    start_B = size // 4
    end_B = size - size // 4 - 1
    if start_B > end_B:
        start_B, end_B = end_B, start_B

    for i in range(size):
        if i == row_with_B:
            row = ['W'] * size
            for j in range(start_B, end_B + 1):
                row[j] = 'B'
            grid.append(''.join(row))

        else:
            grid.append('W' * size)

    # Core logic from original program
    for i in range(size):
        s = grid[i]
        left = s.find('B')
        if left != -1:
            right = s.rfind('B')
            c = (right - left) // 2 + 1
            # print(i + c, left + c)
            pass
            break


if __name__ == "__main__":
    main(10)