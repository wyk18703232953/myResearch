def main(n):
    # Interpret n as the size of a square grid: n x n
    # Generate a deterministic grid of '.' with two 'B's placed deterministically
    m = n
    l = []
    for i in range(n):
        row = ['.'] * m
        l.append(row)

    # Place first 'B' at (0, 0) if n > 0
    if n > 0:
        x1_idx, y1_idx = 0, 0
        l[x1_idx][y1_idx] = 'B'

    # Place second 'B' deterministically if possible
    # For n >= 2, place at (n-1, n-1)
    if n >= 2:
        x2_idx, y2_idx = n - 1, m - 1
        l[x2_idx][y2_idx] = 'B'

    # Convert rows to strings to match original structure
    l = [''.join(row) for row in l]

    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    for i in range(n):
        for j in range(m):
            if l[i][j] == 'B':
                if x1 == 0 and y1 == 0:
                    x1, y1 = [i + 1, j + 1]

                else:
                    x2, y2 = [i + 1, j + 1]
    res = []
    x = 0
    y = 0
    if x2 != 0:
        x = (x2 - x1) // 2
        y = (y2 - y1) // 2
    res.append(x1 + x)
    res.append(y1 + y)
    # print(*res)
    pass
if __name__ == "__main__":
    main(5)