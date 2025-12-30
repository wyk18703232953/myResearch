import random


def solve(n, m, grid):
    # grid: list[str] with length n, each of length m, chars '.' or '*'
    ll = [c == '*' for _ in range(n) for c in grid[n - 1 - r][c_idx]  # reverse rows to match original input order
          for r, row in enumerate(grid) for c_idx, c in enumerate(row)][-n * m:]
    # The above is too convoluted; rebuild ll more directly:
    ll = []
    for row in reversed(grid):  # original code read from top to bottom; we emulate same layout
        for c in row:
            ll.append(c == '*')

    nm = n * m
    # Build RLUD the same way as original
    RLUD = [*[range(i, i + m) for i in range(0, nm, m)],
            *[range(i, nm, m) for i in range(m)]]

    cc = [1000] * nm
    for f in (True, False):
        for r in RLUD:
            v = 0
            for i in r:
                if ll[i]:
                    v += 1
                    if cc[i] > v:
                        cc[i] = v
                else:
                    v = 0
                    cc[i] = 0
        if f:
            ll.reverse()
            cc.reverse()

    cc = [c if c != 1 else 0 for c in cc]

    for f in (True, False):
        for r in RLUD:
            v = 0
            for i in r:
                if v > cc[i]:
                    v -= 1
                else:
                    v = cc[i]
                if v:
                    ll[i] = False
        if f:
            ll.reverse()
            cc.reverse()

    if any(ll):
        return "-1"

    res = []
    for i, c in enumerate(cc):
        if c:
            res.append(f"{i // m + 1} {i % m + 1} {c - 1}")
    return f"{len(res)}\n" + "\n".join(res)


def generate_grid(n, m, density=0.3, rnd=None):
    if rnd is None:
        rnd = random.Random(0)
    grid = []
    for _ in range(n):
        row = ''.join('*' if rnd.random() < density else '.' for _ in range(m))
        grid.append(row)
    return grid


def main(n):
    # 这里根据规模 n 生成测试数据：
    # 设定一个接近正方形的 n x m 网格，使得 n*m ≈ n（总规模）
    # 简单起见，令行数为 max(1, int(n ** 0.5))，列数为 max(1, n // 行数)
    rows = max(1, int(n ** 0.5))
    cols = max(1, n // rows)
    # 若 rows*cols < n，则补到不小于 n
    while rows * cols < n:
        cols += 1

    grid = generate_grid(rows, cols)
    result = solve(rows, cols, grid)
    print(result)


if __name__ == "__main__":
    # 示例：规模为 100
    main(100)