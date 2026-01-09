def main(n):
    # Interpret n as both N and M for an N x N grid
    N = n
    M = n

    # Deterministic grid generation:
    # Pattern: grid[i][j] is '#' if (i + j) % 3 == 0, else '.'
    grid = []
    for i in range(N):
        row = []
        for j in range(M):
            if (i + j) % 3 == 0:
                row.append('#')

            else:
                row.append('.')
        grid.append(row)

    def check(grid, i, j, sx, sy):
        if i - sx >= 0 and j - sy >= 0 and i + 2 - sx < N and j + 2 - sy < M:
            i -= sx
            j -= sy
            v = (
                grid[i][j] == '#' and
                grid[i+1][j] == '#' and
                grid[i+2][j] == '#' and
                grid[i][j+1] == '#' and
                grid[i+2][j+1] == '#' and
                grid[i][j+2] == '#' and
                grid[i+1][j+2] == '#' and
                grid[i+2][j+2] == '#'
            )
            return v
        return False

    for m in range(M):
        for i in range(N):
            if grid[i][m] == '#':
                if not (
                    check(grid, i, m, 0, 0) or
                    check(grid, i, m, 1, 0) or
                    check(grid, i, m, 2, 0) or
                    check(grid, i, m, 0, 1) or
                    check(grid, i, m, 2, 1) or
                    check(grid, i, m, 0, 2) or
                    check(grid, i, m, 1, 2) or
                    check(grid, i, m, 2, 2)
                ):
                    # print("NO")
                    pass
                    return
    # print("YES")
    pass
if __name__ == "__main__":
    main(10)