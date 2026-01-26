import sys
from itertools import accumulate

def list2d(a, b, c):
    return [[c] * b for _ in range(a)]

def list3d(a, b, c, d):
    return [[[d] * c for _ in range(b)] for _ in range(a)]

def list4d(a, b, c, d, e):
    return [[[[e] * d for _ in range(c)] for _ in range(b)] for _ in range(a)]

def ceil(x, y=1):
    return int(-(-x // y))

INF = 10 ** 18
MOD = 10 ** 9 + 7

def build_grid(H, W, intv, _type, space=True, padding=False, raw_grid=None):
    if padding:
        offset = 1

    else:
        offset = 0
    grid = list2d(H + offset * 2, W + offset * 2, intv)
    for i in range(offset, H + offset):
        row = list(map(_type, raw_grid[i - offset])) if space else list(map(_type, raw_grid[i - offset]))
        for j in range(offset, W + offset):
            grid[i][j] = row[j - offset]
    return grid

def run_core(H, W, grid):
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
        output_lines = [str(len(ans))]
        for h, w, sz in ans:
            output_lines.append(f"{h} {w} {sz}")
        return "\n".join(output_lines)

    else:
        return "-1"

def generate_grid(H, W):
    # Deterministic pattern: positions where (i*j) % 3 == 0 are '*', else '.'
    raw_grid = []
    for i in range(H):
        row = []
        for j in range(W):
            if (i + 1) * (j + 1) % 3 == 0:
                row.append('*')

            else:
                row.append('.')
        raw_grid.append("".join(row))
    return raw_grid

def main(n):
    if n < 1:
        n = 1
    H = n
    W = n
    raw_grid = generate_grid(H, W)
    grid = build_grid(H, W, '#', str, space=False, padding=True, raw_grid=raw_grid)
    result = run_core(H, W, grid)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)