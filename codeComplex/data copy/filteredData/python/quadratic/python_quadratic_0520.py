def main(n):
    # Map n to grid size: for time complexity experiments we use an n x n grid
    rows = n
    cols = n

    # Deterministically generate grid b and marker array a
    # Pattern: cell is '#' if (i + j) is even, else '.'
    b = []
    a = []
    for i in range(rows):
        b.append(['#' if (i + j) % 2 == 0 else '.' for j in range(cols)])
        a.append([0 for _ in range(cols)])

    def check(e, r, q):
        if e >= 0 and r >= 0 and e + 2 < rows and r + 2 < cols:
            if (b[e][r] == '#' and b[e + 1][r] == '#' and b[e + 2][r] == '#' and
                b[e + 2][r + 1] == '#' and b[e + 2][r + 2] == '#' and
                b[e + 1][r + 2] == '#' and b[e][r + 2] == '#' and
                b[e][r + 1] == '#'):
                # Mark the 3x3 border in a
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

    for i in range(rows):
        for j in range(cols):
            if b[i][j] == '#':
                if (not check(i, j, 0)) and a[i][j] == 0:
                    # print("NO")
                    pass
                    return
    # print("YES")
    pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)