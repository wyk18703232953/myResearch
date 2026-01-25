def main(n):
    # Map n to grid size: create an n x n grid
    N = n
    M = n

    # Deterministic grid generation:
    # Place '#' in a pattern that ensures some valid 3x3 blocks and some isolated cells
    grid = []
    for i in range(N):
        row = []
        for j in range(M):
            # Simple deterministic rule:
            # Cells where (i//3 + j//3) is even form 3x3 blocks filled with '#'
            # Inside such blocks, mark all positions as '#'
            if ((i // 3) + (j // 3)) % 2 == 0:
                row.append('#')
            else:
                row.append('.')
        grid.append(row)

    def check(grid, i, j, sx, sy):
        if i - sx >= 0 and j - sy >= 0 and i + 2 - sx < N and j + 2 - sy < M:
            i -= sx
            j -= sy
            v = (
                grid[i][j] == '#'
                and grid[i + 1][j] == '#'
                and grid[i + 2][j] == '#'
                and grid[i][j + 1] == '#'
                and grid[i + 2][j + 1] == '#'
                and grid[i][j + 2] == '#'
                and grid[i + 1][j + 2] == '#'
                and grid[i + 2][j + 2] == '#'
            )
            return v
        return False

    prev = False
    for m in range(M):
        for nn in range(N):
            if grid[nn][m] == '#':
                if not (
                    check(grid, nn, m, 0, 0)
                    or check(grid, nn, m, 1, 0)
                    or check(grid, nn, m, 2, 0)
                    or check(grid, nn, m, 0, 1)
                    or check(grid, nn, m, 2, 1)
                    or check(grid, nn, m, 0, 2)
                    or check(grid, nn, m, 1, 2)
                    or check(grid, nn, m, 2, 2)
                ):
                    print("NO")
                    return
    print("YES")


if __name__ == "__main__":
    # Example deterministic call; change n to adjust scale
    main(9)