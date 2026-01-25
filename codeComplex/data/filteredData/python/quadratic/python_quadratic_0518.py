def main(n):
    # Map n to grid size: use n as both rows and columns, with a minimum of 3
    if n < 3:
        n = 3
    rows = n
    cols = n

    m = cols
    dp = [[-1 for _ in range(m)] for _ in range(rows)]
    dp2 = [[-1 for _ in range(m)] for _ in range(rows)]

    # Deterministic generation of the input grid of '.' and '#'
    # Pattern: cell (i,j) is '#' when (i + j) % 2 == 0, else '.'
    for i in range(rows):
        s = ''.join('#' if (i + j) % 2 == 0 else '.' for j in range(cols))
        for j in range(m):
            if s[j] == '.':
                dp[i][j] = -1
            else:
                dp[i][j] = s[j]

    for i in range(0, rows - 2):
        for j in range(0, m - 2):
            p = 0
            c = 0
            for k in range(i, i + 3):
                for h in range(j, j + 3):
                    p = p + 1
                    if p != 5:
                        if dp[k][h] == '#':
                            c = c + 1

            if c == 8:
                p = 0
                for k in range(i, i + 3):
                    for h in range(j, j + 3):
                        p = p + 1
                        if p != 5:
                            dp2[k][h] = '#'

    if dp == dp2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main(5)