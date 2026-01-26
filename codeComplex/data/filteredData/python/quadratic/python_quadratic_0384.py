def main(n):
    # Interpret n as matrix size: n x n
    # Ensure n >= 2 to guarantee at least two 'B's on the diagonal
    if n < 2:
        n = 2

    m = n
    l = []

    # Deterministic construction: matrix with 'B' on the main diagonal at row 0 and row n-1, '.' elsewhere
    for i in range(n):
        row = []
        for j in range(m):
            if i == 0 and j == 0:
                row.append('B')
            elif i == n - 1 and j == n - 1:
                row.append('B')

            else:
                row.append('.')
        l.append(''.join(row))

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