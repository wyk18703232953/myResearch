def main(n):
    # Interpret n as both number of rows and columns for scalability
    rows = n
    cols = n

    # Generate a deterministic grid of '#' and '.'
    # Pattern: cell (i, j) is '#' if (i + j) % 3 != 0, else '.'
    s = []
    st = set()
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 != 0:
                ch = '#'
                st.add((i, j))

            else:
                ch = '.'
            row_chars.append(ch)
        s.append("".join(row_chars))

    cst = set()
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
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
    main(10)