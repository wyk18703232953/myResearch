def main(n):
    # Map n to a grid of approximate size sqrt(n) x sqrt(n)
    if n < 3:
        n = 3
    import math
    rows = max(3, int(math.isqrt(n)))
    cols = max(3, int(math.isqrt(n)))

    # Deterministically generate grid a of '#' and '.' with a pattern
    a = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Simple periodic pattern based on i, j
            if (i + j) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        a.append(row)

    # Core algorithm (unchanged logic, adapted to generated a, rows, cols)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            may = True
            if (
                a[i][j - 1] == '.' or
                a[i][j + 1] == '.' or
                a[i + 1][j - 1] == '.' or
                a[i + 1][j + 1] == '.' or
                a[i + 1][j] == '.' or
                a[i - 1][j - 1] == '.' or
                a[i - 1][j + 1] == '.' or
                a[i - 1][j] == '.'
            ):
                may = False
            if may:
                a[i][j - 1] = a[i][j + 1] = a[i + 1][j - 1] = a[i + 1][j + 1] = a[i + 1][j] = a[i - 1][j - 1] = a[i - 1][j + 1] = a[i - 1][j] = '?'

    for i in range(rows):
        for j in range(cols):
            if a[i][j] == '#':
                # print("NO")
                pass
                return
    # print("YES")
    pass
if __name__ == "__main__":
    main(1000)