n_default, m_default = 5, 7

def generate_input(n):
    n_rows = max(1, n)
    m_cols = m_default
    grid = []
    center_row = n_rows // 2
    start_col = max(0, (m_cols - n_rows) // 2)
    for i in range(n_rows):
        if i == center_row:
            row = ['.'] * m_cols
            for j in range(start_col, min(start_col + n_rows, m_cols)):
                row[j] = 'B'
            grid.append(''.join(row))
        else:
            grid.append('.' * m_cols)
    return n_rows, m_cols, grid

def core_algorithm(n, m, grid):
    lock = 0
    Ccen = 0
    Rcen = 0
    for i in range(n):
        s = str(grid[i])
        if (('B' in s) and (lock == 0)):
            Rstart = s.index('B')
            cnt = s.count('B')
            Rcen = Rstart + (cnt // 2)
            Cstart = i
            Ccen = Cstart + (cnt // 2)
            lock = 1
    return Ccen + 1, Rcen + 1

def main(n):
    n_gen, m_gen, grid = generate_input(n)
    row_center, col_center = core_algorithm(n_gen, m_gen, grid)
    print(row_center, col_center)

if __name__ == "__main__":
    main(5)