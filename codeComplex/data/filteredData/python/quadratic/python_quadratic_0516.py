def main(n):
    # Map n to a square grid of size n x n for scalability
    rows = n
    cols = n
    # Deterministic generation of grid a: pattern based on indices
    # Use '#' when (i + j) % 3 == 0, else '.'
    a = []
    for i in range(rows):
        row_chars = ['#' if (i + j) % 3 == 0 else '.' for j in range(cols)]
        a.append(''.join(row_chars))

    # Original logic with n -> rows, m -> cols
    for i in range(rows):
        for j in range(cols):
            if a[i][j] == '.':
                continue
            if i >= 2 and j >= 2:
                if a[i-2][j-2] == '#' and a[i-2][j-1] == '#' and a[i-2][j] == '#' \
                        and a[i-1][j] == '#' and a[i-1][j-2] == '#' and a[i][j-1] == '#' and a[i][j-2] == '#':
                    continue
            if i >= 1 and i <= rows-2 and j >= 2 and a[i-1][j-2] == '#' and a[i-1][j-1] == '#' and a[i-1][j] == '#' \
                    and a[i][j-2] == '#' and a[i+1][j-2] == '#' and a[i+1][j-1] == '#' and a[i+1][j] == '#':
                continue
            if i <= rows-3 and j >= 2 and a[i][j-1] == '#' and a[i][j-2] == '#' and a[i+1][j] == '#' \
                    and a[i+1][j-2] == '#' and a[i+2][j] == '#' and a[i+2][j-1] == '#' and a[i+2][j-2] == '#':
                continue
            if i <= rows-3 and j >= 1 and j <= cols-2 and a[i][j-1] == '#' and a[i][j+1] == '#' and a[i+1][j-1] == '#' \
                    and a[i+1][j+1] == '#' and a[i+2][j] == '#' and a[i+2][j-1] == '#' and a[i+2][j+1] == '#':
                continue
            if i <= rows-3 and j <= cols-3 and a[i][j+1] == '#' and a[i][j+2] == '#' and a[i+1][j] == '#' \
                    and a[i+1][j+2] == '#' and a[i+2][j] == '#' and a[i+2][j+1] == '#' and a[i+2][j+2] == '#':
                continue
            if i <= rows-2 and i >= 1 and j <= cols-3 and a[i-1][j] == '#' and a[i-1][j+1] == '#' and a[i-1][j+2] == '#' \
                    and a[i][j+2] == '#' and a[i+1][j] == '#' and a[i+1][j+1] == '#' and a[i+1][j+2] == '#':
                continue
            if i >= 2 and j <= cols-3 and a[i-2][j] == '#' and a[i-2][j+1] == '#' and a[i-2][j+2] == '#' \
                    and a[i-1][j] == '#' and a[i-1][j+2] == '#' and a[i][j+1] == '#' and a[i][j+2] == '#':
                continue
            if i >= 2 and j <= cols-2 and j >= 1 and a[i-2][j-1] == '#' and a[i-2][j] == '#' and a[i-2][j+1] == '#' \
                    and a[i-1][j-1] == '#' and a[i-1][j+1] == '#' and a[i][j-1] == '#' and a[i][j+1] == '#':
                continue
            # print('NO')
            pass
            return 'NO'
    # print('YES')
    pass
    return 'YES'


if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)