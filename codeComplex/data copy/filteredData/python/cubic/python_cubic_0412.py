def helper(n, m, k, hedge, vedge):
    if k % 2 == 1:
        res = [[-1] * m for _ in range(n)]
        return res

    k = k // 2
    pool = [[[0] * m for _ in range(n)] for _ in range(k + 1)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for t in range(1, k + 1):
        for i in range(n):
            for j in range(m):
                tres = [9999999] * 4
                for c in range(4):
                    ni = i + dx[c]
                    nj = j + dy[c]
                    if 0 <= ni < n and 0 <= nj < m:
                        if c == 0:
                            tres[c] = hedge[i][j] * 2 + pool[t - 1][ni][nj]
                        elif c == 1:
                            tres[c] = hedge[i][j - 1] * 2 + pool[t - 1][ni][nj]
                        elif c == 2:
                            tres[c] = vedge[i][j] * 2 + pool[t - 1][ni][nj]

                        else:
                            tres[c] = vedge[i - 1][j] * 2 + pool[t - 1][ni][nj]
                pool[t][i][j] = min(tres)

    return pool[k]


def generate_data(n):
    # Interpret n as grid size; keep k as an even, deterministic function of n.
    if n <= 0:
        n = 1
    m = n
    # Ensure k is even and at least 2 for meaningful paths when n>1
    k = (2 * n) if n > 1 else 2

    hedge = [[(i + j + 1) for j in range(m - 1)] for i in range(n)]
    vedge = [[(i + j + 2) for j in range(m)] for i in range(n - 1)]
    return n, m, k, hedge, vedge


def main(n):
    n_grid, m, k, hedge, vedge = generate_data(n)
    res = helper(n_grid, m, k, hedge, vedge)
    for row in res:
        # print(" ".join(map(str, row)))
        pass
if __name__ == "__main__":
    main(5)