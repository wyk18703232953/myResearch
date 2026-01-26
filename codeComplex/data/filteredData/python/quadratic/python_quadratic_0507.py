def main(n):
    # Map n to grid size: use n x n grid, but at least 3x3 to allow pattern checks
    if n < 3:
        n = 3
    m = n

    # Deterministically generate grid s of size n x m with '#' and '.'
    # Pattern: s[i][j] is '#' iff (i * m + j) % 3 == 0
    s = []
    st = set()
    cst = set()

    for i in range(n):
        row_chars = []
        for j in range(m):
            if (i * m + j) % 3 == 0:
                row_chars.append('#')
                st.add((i, j))

            else:
                row_chars.append('.')
        s.append(''.join(row_chars))

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if s[i - 1][j - 1] != '#':
                continue
            if s[i - 1][j] != '#':
                continue
            if s[i - 1][j + 1] != '#':
                continue
            if s[i][j - 1] != '#':
                continue
            if s[i][j + 1] != '#':
                continue
            if s[i + 1][j - 1] != '#':
                continue
            if s[i + 1][j] != '#':
                continue
            if s[i + 1][j + 1] != '#':
                continue
            cst.add((i - 1, j))
            cst.add((i - 1, j - 1))
            cst.add((i - 1, j + 1))
            cst.add((i + 1, j))
            cst.add((i + 1, j - 1))
            cst.add((i + 1, j + 1))
            cst.add((i, j + 1))
            cst.add((i, j - 1))

    if len(cst) == len(st):
        # print('YES')
        pass

    else:
        # print('NO')
        pass
if __name__ == "__main__":
    # Example deterministic call for experimentation
    main(10)