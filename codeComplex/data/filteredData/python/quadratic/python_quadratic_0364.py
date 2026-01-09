def main(n):
    # Map n to grid size H x W
    # For time complexity experiments, we choose H = W = n
    H = n
    W = n

    # Helper functions (deterministic, no I/O)
    def list2d(a, b, c):
        return [[c] * b for _ in range(a)]

    INF = 10 ** 18
    MOD = 10 ** 9 + 7

    # Deterministic grid generator replacing build_grid + stdin input
    # Original grid was HxW of characters ('.' or '*'), padded by 1 around
    # We construct a pattern depending only on H,W so it's fully deterministic.
    # Pattern: for each cell (i,j) in [0,H-1]x[0,W-1], put '*'
    # except when (i+j) % 3 == 0, put '.'
    base_grid = []
    for i in range(H):
        row = []
        for j in range(W):
            if (i + j) % 3 == 0:
                row.append('.')

            else:
                row.append('*')
        base_grid.append(row)

    # Build padded grid as in original build_grid(..., padding=1)
    grid = list2d(H + 2, W + 2, '#')
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            grid[i][j] = base_grid[i - 1][j - 1]

    ans = []
    imosw = list2d(H + 2, W + 2, 0)
    imosh = list2d(H + 2, W + 2, 0)

    L = list2d(H + 2, W + 2, 0)
    R = list2d(H + 2, W + 2, 0)
    U = list2d(H + 2, W + 2, 0)
    D = list2d(H + 2, W + 2, 0)

    def check(i, j):
        sz = min(L[i][j], R[i][j], U[i][j], D[i][j])
        if sz > 1:
            imosw[i][j - sz + 1] += 1
            imosw[i][j + sz] -= 1
            imosh[i - sz + 1][j] += 1
            imosh[i + sz][j] -= 1
            ans.append((i, j, sz - 1))

    def check2():
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                if grid[i][j] == '*' and not imosw[i][j] and not imosh[i][j]:
                    return False
        return True

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '.':
                L[i][j] = 0

            else:
                L[i][j] = L[i][j - 1] + 1

    for i in range(1, H + 1):
        for j in range(W, 0, -1):
            if grid[i][j] == '.':
                R[i][j] = 0

            else:
                R[i][j] = R[i][j + 1] + 1

    for j in range(1, W + 1):
        for i in range(1, H + 1):
            if grid[i][j] == '.':
                U[i][j] = 0

            else:
                U[i][j] = U[i - 1][j] + 1

    for j in range(1, W + 1):
        for i in range(H, 0, -1):
            if grid[i][j] == '.':
                D[i][j] = 0

            else:
                D[i][j] = D[i + 1][j] + 1

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '*':
                check(i, j)

    for i in range(1, H + 1):
        for j in range(W + 1):
            imosw[i][j + 1] += imosw[i][j]

    for j in range(1, W + 1):
        for i in range(H + 1):
            imosh[i + 1][j] += imosh[i][j]

    if check2():
        # print(len(ans))
        pass
        for h, w, sz in ans:
            # print(h, w, sz)
            pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    # Example: run with n = 5
    main(5)