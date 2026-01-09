import math


def around(x, y, hor, ver, mtx, n, m):
    a, b, c, d = [math.inf] * 4

    if x > 0:
        a = hor[y][x - 1] * 2 + mtx[y][x - 1]

    if x < m - 1:
        b = hor[y][x] * 2 + mtx[y][x + 1]

    if y > 0:
        c = ver[y - 1][x] * 2 + mtx[y - 1][x]

    if y < n - 1:
        d = ver[y][x] * 2 + mtx[y + 1][x]

    return min(a, b, c, d)


def generate_input(n):
    if n < 2:
        n = 2
    # Matrix size n x n, step count k derived from n
    rows = n
    cols = n
    k = 2 * n  # even, grows linearly with n

    # Deterministic generation of matrices hor (rows x (cols-1)) and ver ((rows-1) x cols)
    hor = [[(i * cols + j) % 7 + 1 for j in range(cols - 1)] for i in range(rows)]
    ver = [[(i * cols + j * 2 + 3) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]
    return rows, cols, k, hor, ver


def main(n):
    n_rows, m_cols, k, hor, ver = generate_input(n)

    if k % 2:
        result = []
        for _ in range(n_rows):
            result.append([-1] * m_cols)
        return result

    current = [[0] * m_cols for _ in range(n_rows)]
    for _ in range(k // 2):
        new = [[0] * m_cols for _ in range(n_rows)]
        for x in range(m_cols):
            for y in range(n_rows):
                new[y][x] = around(x, y, hor, ver, current, n_rows, m_cols)
        current = new

    return current


if __name__ == "__main__":
    n = 5
    res = main(n)
    for row in res:
        # print(*row)
        pass