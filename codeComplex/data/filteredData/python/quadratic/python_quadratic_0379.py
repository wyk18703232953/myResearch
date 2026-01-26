def main(n):
    # Interpret n as both number of rows and columns of the grid
    rows = n
    cols = n

    # Deterministic grid generation:
    # Place a contiguous block of 'B's in row r0 from column c0 to c1 (inclusive)
    if n == 0:
        return

    r0 = n // 3
    c0 = n // 4
    c1 = min(n - 1, c0 + max(1, n // 5))

    # Ensure indices are within bounds
    if r0 >= n:
        r0 = n - 1
    if c0 >= n:
        c0 = 0
    if c1 < c0:
        c1 = c0

    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if i == r0 and c0 <= j <= c1:
                row_chars.append('B')

            else:
                row_chars.append('.')
        s = ''.join(row_chars)

        left = s.find('B')
        if left != -1:
            right = s.rfind('B')
            c = (right - left) // 2 + 1
            # print(i + c, left + c)
            pass
            break


if __name__ == "__main__":
    main(10)