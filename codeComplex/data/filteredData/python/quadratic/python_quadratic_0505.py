def main(n):
    # Define grid size based on n
    if n < 3:
        n_rows = 3
        m_cols = 3
    else:
        n_rows = n
        m_cols = n

    # Deterministically generate the input grid as list of strings
    # Pattern: '#' when (i+j) is even, '.' otherwise
    mp = []
    for i in range(n_rows):
        row = []
        for j in range(m_cols):
            if (i + j) % 2 == 0:
                row.append(True)   # '#'
            else:
                row.append(False)  # '.'
        mp.append(row)

    mp1 = [[False for _ in range(m_cols)] for _ in range(n_rows)]

    for i in range(1, n_rows - 1):
        for j in range(1, m_cols - 1):
            f = all(mp[i - 1][j - k] for k in range(-1, 1 + 1))
            f = f and all(mp[i + 1][j - k] for k in range(-1, 1 + 1))
            f = f and (mp[i][j - 1] and mp[i][j + 1])

            if not f:
                continue

            for ik in range(-1, 2):
                for jk in range(-1, 2):
                    if ik == 0 and jk == 0:
                        continue
                    mp1[i + ik][j + jk] = True

    if all(all(mp[i][j] == mp1[i][j] for j in range(m_cols)) for i in range(n_rows)):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main(10)