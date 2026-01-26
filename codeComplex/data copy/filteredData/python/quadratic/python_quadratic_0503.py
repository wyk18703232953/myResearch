def main(n):
    # Interpret n as both dimensions of the grid: n x n
    if n < 3:
        # For grids smaller than 3x3, the inner loops won't run; just build and check.
        m = n

    else:
        m = n

    # Deterministic grid generation: pattern based on indices
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            # Place '#' where (i+j) is even and inside the border, otherwise '.'
            if 0 < i < n - 1 and 0 < j < m - 1 and (i + j) % 2 == 0:
                row.append('#')

            else:
                row.append('.')
        a.append(row)

    # Core logic preserved from original program
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            may = True
            if (a[i][j - 1] == '.' or
                a[i][j + 1] == '.' or
                a[i + 1][j - 1] == '.' or
                a[i + 1][j + 1] == '.' or
                a[i + 1][j] == '.' or
                a[i - 1][j - 1] == '.' or
                a[i - 1][j + 1] == '.' or
                a[i - 1][j] == '.'):
                may = False
            if may:
                a[i][j - 1] = a[i][j + 1] = a[i + 1][j - 1] = a[i + 1][j + 1] = a[i + 1][j] = a[i - 1][j - 1] = a[i - 1][j + 1] = a[i - 1][j] = '?'

    for i in range(n):
        for j in range(m):
            if a[i][j] == '#':
                # print("NO")
                pass
                return
    # print("YES")
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)