def main(n):
    # Interpret n as grid size; derive m and k deterministically from n
    if n <= 0:
        return
    m = n
    # Ensure k is even to exercise the inner DP loop; scale with n
    k = (2 * n) if n % 2 == 0 else (2 * n + 2)

    # Deterministic generation of hor and ver with the same shape as original input
    # hor: n rows, m-1 edges each (horizontal weights between columns)
    hor = [[(i * m + j) % 7 + 1 for j in range(m - 1)] for i in range(n)]
    # ver: n-1 rows, m edges each (vertical weights between rows)
    ver = [[(i * m + j * 2 + 3) % 9 + 1 for j in range(m)] for i in range(n - 1)]

    mtx_old = [[0] * m for _ in range(n)]

    def neighbours(x, y):
        a = 1e18
        b = 1e18
        c = 1e18
        d = 1e18
        if x > 0:
            a = hor[y][x - 1] * 2 + mtx_old[y][x - 1]
        if x < m - 1:
            b = hor[y][x] * 2 + mtx_old[y][x + 1]
        if y > 0:
            c = ver[y - 1][x] * 2 + mtx_old[y - 1][x]
        if y < n - 1:
            d = ver[y][x] * 2 + mtx_old[y + 1][x]
        return min(a, b, c, d)

    for _ in range(k // 2):
        mtx_new = [[0] * m for _ in range(n)]
        for x in range(m):
            for y in range(n):
                mtx_new[y][x] = neighbours(x, y)
        mtx_old = mtx_new

    for row in mtx_old:
        # print(*row)
        pass
if __name__ == "__main__":
    main(5)