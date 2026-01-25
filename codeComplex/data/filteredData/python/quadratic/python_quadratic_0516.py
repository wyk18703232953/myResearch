def main(n):
    # 映射：原程序中的 n,m 都取为输入规模 n
    rows = n
    cols = n
    if rows <= 0 or cols <= 0:
        print("YES")
        return

    # 构造一个确定性的 rows x cols 网格
    # 规则：位置 (i,j) 为 '#' 当且仅当 (i + j) % 3 == 0，否则为 '.'
    a = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            if (i + j) % 3 == 0:
                row_chars.append('#')
            else:
                row_chars.append('.')
        a.append(''.join(row_chars))

    n_local, m_local = rows, cols

    for i in range(n_local):
        for j in range(m_local):
            if a[i][j] == '.':
                continue
            if i >= 2 and j >= 2:
                if a[i-2][j-2] == '#' and a[i-2][j-1] == '#' and a[i-2][j] == '#' \
                        and a[i-1][j] == '#' and a[i-1][j-2] == '#' and a[i][j-1] == '#' and a[i][j-2] == '#':
                    continue
            if i >= 1 and i <= n_local-2 and j >= 2 and a[i-1][j-2] == '#' and a[i-1][j-1] == '#' and a[i-1][j] == '#' \
                    and a[i][j-2] == '#' and a[i+1][j-2] == '#' and a[i+1][j-1] == '#' and a[i+1][j] == '#':
                continue
            if i <= n_local-3 and j >= 2 and a[i][j-1] == '#' and a[i][j-2] == '#' and a[i+1][j] == '#' \
                    and a[i+1][j-2] == '#' and a[i+2][j] == '#' and a[i+2][j-1] == '#' and a[i+2][j-2] == '#':
                continue
            if i <= n_local-3 and j >= 1 and j <= m_local-2 and a[i][j-1] == '#' and a[i][j+1] == '#' and a[i+1][j-1] == '#' \
                    and a[i+1][j+1] == '#' and a[i+2][j] == '#' and a[i+2][j-1] == '#' and a[i+2][j+1] == '#':
                continue
            if i <= n_local-3 and j <= m_local-3 and a[i][j+1] == '#' and a[i][j+2] == '#' and a[i+1][j] == '#' \
                    and a[i+1][j+2] == '#' and a[i+2][j] == '#' and a[i+2][j+1] == '#' and a[i+2][j+2] == '#':
                continue
            if i <= n_local-2 and i >= 1 and j <= m_local-3 and a[i-1][j] == '#' and a[i-1][j+1] == '#' and a[i-1][j+2] == '#' \
                    and a[i][j+2] == '#' and a[i+1][j] == '#' and a[i+1][j+1] == '#' and a[i+1][j+2] == '#':
                continue
            if i >= 2 and j <= m_local-3 and a[i-2][j] == '#' and a[i-2][j+1] == '#' and a[i-2][j+2] == '#' \
                    and a[i-1][j] == '#' and a[i-1][j+2] == '#' and a[i][j+1] == '#' and a[i][j+2] == '#':
                continue
            if i >= 2 and j <= m_local-2 and j >= 1 and a[i-2][j-1] == '#' and a[i-2][j] == '#' and a[i-2][j+1] == '#' \
                    and a[i-1][j-1] == '#' and a[i-1][j+1] == '#' and a[i][j-1] == '#' and a[i][j+1] == '#':
                continue
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    # 示例：以 n=5 作为规模调用
    main(5)