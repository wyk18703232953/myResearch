from collections import defaultdict, deque
from heapq import heappush, heappop
from math import inf

def solve(n, m, grid):
    A = [[0 for _ in range(m)] for __ in range(n)]
    left = [[0 for _ in range(m)] for __ in range(n)]
    right = [[0 for _ in range(m)] for __ in range(n)]
    up = [[0 for _ in range(m)] for __ in range(n)]
    down = [[0 for _ in range(m)] for __ in range(n)]
    for r in range(n):
        lst = grid[r]
        for c in range(m):
            if lst[c] == '*':
                A[r][c] = left[r][c] = right[r][c] = up[r][c] = down[r][c] = 1

    for r in range(n):
        for c in range(1, m):
            if A[r][c]:
                left[r][c] += left[r][c-1]
        for c in range(m-2, -1, -1):
            if A[r][c]:
                right[r][c] += right[r][c+1]

    for c in range(m):
        for r in range(1, n):
            if A[r][c]:
                up[r][c] += up[r-1][c]
        for r in range(n-2, -1, -1):
            if A[r][c]:
                down[r][c] += down[r+1][c]

    res = []
    stars = 0

    ROWS = [[0 for _ in range(m)] for __ in range(n)]
    COLS = [[0 for _ in range(m)] for __ in range(n)]

    for r in range(n):
        for c in range(m):
            if A[r][c]:
                can = min(left[r][c], right[r][c], up[r][c], down[r][c])
                can -= 1
                if can > 0:
                    stars += 1
                    res.append((r+1, c+1, can))
                ROWS[r-can][c] += can
                if r+can+1 < n:
                    ROWS[r+can+1][c] -= can
                COLS[r][c-can] += can
                if c+can+1 < m:
                    COLS[r][c+can+1] -= can

    valid = [[False for _ in range(m)] for __ in range(n)]
    for r in range(n):
        curr = 0
        for c in range(m):
            curr += COLS[r][c]
            if curr > 0:
                valid[r][c] = True

    for c in range(m):
        curr = 0
        for r in range(n):
            curr += ROWS[r][c]
            if curr > 0:
                valid[r][c] = True

    for r in range(n):
        for c in range(m):
            if A[r][c] and not valid[r][c]:
                # print(-1)
                pass
                return
    # print(stars)
    pass
    for x, y, z in res:
        # print(x, y, z)
        pass

def generate_grid(n):
    # Use n as both rows and columns to scale the 2D input size.
    size = max(1, n)
    grid = []
    for r in range(size):
        row_chars = []
        for c in range(size):
            # Deterministic pattern based on r and c
            # Example: star if (r + c) is even, dot otherwise
            if (r + c) % 2 == 0:
                row_chars.append('*')

            else:
                row_chars.append('.')
        grid.append(''.join(row_chars))
    return grid

def main(n):
    n_int = int(n)
    if n_int <= 0:
        n_int = 1
    grid = generate_grid(n_int)
    solve(n_int, n_int, grid)

if __name__ == "__main__":
    main(5)