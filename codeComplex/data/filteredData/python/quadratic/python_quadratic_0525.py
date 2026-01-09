def main(n):
    # Map n to grid size: use n as both rows and cols (at least 3)
    n = max(3, n)
    m = n

    # Deterministic generation of grid a (n x m) of '.' and '#'
    # Example pattern: a[i][j] is '#' if (i*j) % 7 < 3 else '.'
    a = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i * j) % 7 < 3:
                row.append('#')

            else:
                row.append('.')
        a.append(row)

    b = [list('.' * m) for _ in range(n)]
    start = 0

    for i in range(n):
        if start == 0:
            if '.' in a[i]:
                start = ((i - 3) // 3) * 3
    for i in range(start):
        b[i] = list('#' * m)

    for i in range(start, n - 2):
        for j in range(m - 2):
            ok = True
            if a[i][j] == '#':
                for y in range(i, i + 3):
                    if not ok:
                        break
                    for x in range(j, j + 3):
                        if not ((y == i + 1) and (x == j + 1)):
                            if a[y][x] != '#':
                                ok = False
                                break
                if ok:
                    for y in range(i, i + 3):
                        for x in range(j, j + 3):
                            if not ((y == i + 1) and (x == j + 1)):
                                b[y][x] = '#'

    if a == b:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(10)