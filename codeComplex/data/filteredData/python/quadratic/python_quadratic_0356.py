def main(n):
    # Interpret n as both dimensions of the grid: n x n
    rows = n
    cols = n

    # Deterministic grid generation:
    # Put '*' where (r + c) is even, '.' otherwise.
    A = [[0 for _ in range(cols)] for __ in range(rows)]
    left = [[0 for _ in range(cols)] for __ in range(rows)]
    right = [[0 for _ in range(cols)] for __ in range(rows)]
    up = [[0 for _ in range(cols)] for __ in range(rows)]
    down = [[0 for _ in range(cols)] for __ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2 == 0:
                A[r][c] = left[r][c] = right[r][c] = up[r][c] = down[r][c] = 1

    # Precompute left and right
    for r in range(rows):
        for c in range(1, cols):
            if A[r][c]:
                left[r][c] += left[r][c-1]
        for c in range(cols-2, -1, -1):
            if A[r][c]:
                right[r][c] += right[r][c+1]

    # Precompute up and down
    for c in range(cols):
        for r in range(1, rows):
            if A[r][c]:
                up[r][c] += up[r-1][c]
        for r in range(rows-2, -1, -1):
            if A[r][c]:
                down[r][c] += down[r+1][c]

    res = []
    stars = 0

    ROWS = [[0 for _ in range(cols)] for __ in range(rows)]
    COLS = [[0 for _ in range(cols)] for __ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if A[r][c]:
                can = min(left[r][c], right[r][c], up[r][c], down[r][c])
                can -= 1
                if can > 0:
                    stars += 1
                    res.append((r+1, c+1, can))
                if r - can >= 0:
                    ROWS[r-can][c] += can
                if r+can+1 < rows:
                    ROWS[r+can+1][c] -= can
                if c - can >= 0:
                    COLS[r][c-can] += can
                if c+can+1 < cols:
                    COLS[r][c+can+1] -= can

    valid = [[False for _ in range(cols)] for __ in range(rows)]
    for r in range(rows):
        curr = 0
        for c in range(cols):
            curr += COLS[r][c]
            if curr > 0:
                valid[r][c] = True

    for c in range(cols):
        curr = 0
        for r in range(rows):
            curr += ROWS[r][c]
            if curr > 0:
                valid[r][c] = True

    for r in range(rows):
        for c in range(cols):
            if A[r][c] and not valid[r][c]:
                # print(-1)
                pass
                return

    # print(stars)
    pass
    for x, y, z in res:
        # print(x, y, z)
        pass
if __name__ == "__main__":
    main(5)