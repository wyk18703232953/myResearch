def color8(i, j, ip, n, m):
    if i > n - 3 or j > m - 3:
        return
    ip[i][j] = '#'
    ip[i][j + 1] = '#'
    ip[i][j + 2] = '#'
    ip[i + 1][j] = '#'
    ip[i + 1][j + 2] = '#'
    ip[i + 2][j] = '#'
    ip[i + 2][j + 1] = '#'
    ip[i + 2][j + 2] = '#'


def run_once(grid):
    n = len(grid)
    m = len(grid[0]) if n > 0 else 0
    ip = grid
    op = [['.' for _ in range(m)] for _ in range(n)]
    b = 0
    for i in range(n):
        for j in range(m):
            if ip[i][j] == '#':
                try:
                    if ip[i + 2][j + 2] == '#':
                        temp = (
                            ip[i][j] == '#' and
                            ip[i][j + 1] == '#' and
                            ip[i][j + 2] == '#' and
                            ip[i + 1][j] == '#' and
                            ip[i + 1][j + 2] == '#' and
                            ip[i + 2][j] == '#' and
                            ip[i + 2][j + 1] == '#' and
                            ip[i + 2][j + 2] == '#'
                        )
                        if temp:
                            color8(i, j, op, n, m)
                except IndexError:
                    pass
    for i in range(n):
        if ''.join(op[i]) != ip[i]:
            return "NO"
    return "YES"


def generate_grid(n):
    # Define a deterministic mapping from n to (rows, cols)
    rows = n
    cols = max(1, n // 2)

    # Build a deterministic grid pattern using simple arithmetic
    grid = []
    for i in range(rows):
        row_chars = []
        for j in range(cols):
            # Deterministic pattern: place '#' when (i + j * 2) % 5 == 0
            if (i + 2 * j) % 5 == 0:
                row_chars.append('#')
            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))
    return grid


def main(n):
    grid = generate_grid(n)
    result = run_once(grid)
    print(result)


if __name__ == "__main__":
    main(10)