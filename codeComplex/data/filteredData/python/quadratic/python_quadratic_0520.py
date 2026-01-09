def main(n):
    # Interpret n as both the number of rows and columns
    # Ensure minimum size 3 to allow 3x3 patterns
    if n < 1:
        return
    global b, a
    b = []
    a = []
    m = n

    # Deterministic grid generation:
    # Create a pattern where some 3x3 border-# blocks exist and others don't.
    # Rule: cell (i,j) is '#' if (i//3 + j//3) is even, else '.'
    for i in range(n):
        row = []
        for j in range(m):
            if ((i // 3) + (j // 3)) % 2 == 0:
                row.append('#')

            else:
                row.append('.')
        b.append(row)
        a.append([0 for _ in range(m)])

    def check(e, r, q):
        if e >= 0 and r >= 0 and e + 2 < n and r + 2 < m:
            if (b[e][r] == '#' and b[e + 1][r] == '#' and b[e + 2][r] == '#' and
                b[e + 2][r + 1] == '#' and b[e + 2][r + 2] == '#' and
                b[e + 1][r + 2] == '#' and b[e][r + 2] == '#' and b[e][r + 1] == '#'):
                a[e][r] = 1
                a[e + 1][r] = 1
                a[e + 2][r] = 1
                a[e + 2][r + 1] = 1
                a[e + 2][r + 2] = 1
                a[e + 1][r + 2] = 1
                a[e][r + 2] = 1
                a[e][r + 1] = 1
                return True
        if q == 1:
            return False
        return (check(e, r - 1, 1) or check(e, r - 2, 1) or
                check(e - 1, r - 2, 1) or check(e - 2, r - 2, 1) or
                check(e - 2, r - 1, 1) or check(e - 2, r, 1) or
                check(e - 1, r, 1))

    for i in range(n):
        for j in range(m):
            if b[i][j] == '#':
                if (not check(i, j, 0)) and a[i][j] == 0:
                    # print("NO")
                    pass
                    return
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)