def main(n):
    # Interpret n as both dimensions of the grid: n rows, n columns
    # Ensure minimum size of 3 to allow the original 3x3 pattern logic
    if n < 3:
        # print("NO")
        pass
        return

    m = n

    # Deterministic grid generation:
    # Place the exact pattern that the original algorithm tries to reconstruct
    # at the top-left corner (positions around (0,0)), and fill the rest with dots.
    u = []
    for i in range(n):
        row = []
        for j in range(m):
            # Pattern shape (relative to (0,0)):
            # (0,0) (0,1) (0,2)
            # (1,0)      (1,2)
            # (2,0) (2,1) (2,2)
            if i <= 2 and j <= 2:
                # Inside 3x3 block, follow the pattern
                if (i == 1 and j == 1):
                    row.append('.')  # center is '.'

                else:
                    row.append('#')

            else:
                row.append('.')
        u.append(row)

    # Copy of original logic, using generated u and computed m
    u1 = []
    for i in range(n):
        u1.append(['.'] * m)

    for i in range(n - 2):
        for j in range(m - 2):
            ok = True
            for k in range(3):
                if u[i][j + k] != '#' or u[i + k][j] != '#':
                    ok = False
                    break
            if ok:
                if u[i + 2][j + 1] != '#' or u[i + 2][j + 2] != '#' or u[i + 1][j + 2] != '#':
                    ok = False

                else:
                    for k in range(3):
                        u1[i][j + k] = '#'
                        u1[i + k][j] = '#'
                    u1[i + 2][j + 1] = '#'
                    u1[i + 2][j + 2] = '#'
                    u1[i + 1][j + 2] = '#'

    ok = True
    for i in range(n):
        for j in range(m):
            if u[i][j] != u1[i][j]:
                ok = False
                break
        if not ok:
            break

    if ok:
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    main(5)