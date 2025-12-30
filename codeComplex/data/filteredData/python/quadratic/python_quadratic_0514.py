import random

# 8-neighborhood directions
rnd = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
)


def gene(x, y, p, n, m):
    # generate 8 cells of a pattern centered so that one cell is (x,y) with direction p
    cx = x - rnd[p][0]
    cy = y - rnd[p][1]
    ans = []
    for i in range(8):
        ans.append((cx + rnd[i][0], cy + rnd[i][1]))
    return ans


def judge(ps, grid, n, m):
    # check whether all cells in ps are inside grid and all are '#'
    for x, y in ps:
        if 0 <= x < n and 0 <= y < m and grid[x][y] == '#':
            continue
        else:
            return False
    return True


def dye(ps, marked):
    # mark cells in ps as covered
    for x, y in ps:
        marked[x][y] = True


def check(x, y, grid, marked, n, m):
    # check if there exists a pattern covering (x,y)
    for i in range(8):
        r = gene(x, y, i, n, m)
        if judge(r, grid, n, m):
            dye(r, marked)
            return True
    return False


def generate_test_grid(n, m):
    # generate a random grid with '#' and '.'; ensure n,m >= 3 to allow patterns
    # probability controls density of '#'
    prob_hash = 0.4
    grid = []
    for _ in range(n):
        row = ''.join('#' if random.random() < prob_hash else '.' for _ in range(m))
        grid.append(row)
    return grid


def main(n):
    # choose m based on n; here we simply set m = n or at least 3
    m = max(3, n)

    # generate test data: an n x m grid
    s = generate_test_grid(n, m)

    # marked cells initially False
    mapp = [[False] * m for _ in range(n)]

    # core logic from original program
    for i in range(n):
        for j in range(m):
            if s[i][j] == '#' and mapp[i][j] is False:
                if check(i, j, s, mapp, n, m):
                    continue
                else:
                    print('NO')
                    return
    print('YES')


if __name__ == "__main__":
    # example run with n = 10
    main(10)