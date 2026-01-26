import sys
from math import inf


def explorer(n, m, k, R, C):
    if k % 2:
        return None

    G = [[0] * m for _ in range(n)]
    G_ = [[0] * m for _ in range(n)]
    for _ in range(k // 2):
        for i in range(n):
            for j in range(m):
                x = inf
                if i > 0:
                    x = min(x, G[i - 1][j] + 2 * C[i - 1][j])
                if i + 1 < n:
                    x = min(x, G[i + 1][j] + 2 * C[i][j])
                if j > 0:
                    x = min(x, G[i][j - 1] + 2 * R[i][j - 1])
                if j + 1 < m:
                    x = min(x, G[i][j + 1] + 2 * R[i][j])
                G_[i][j] = x
        G, G_ = G_, G
    return G


def lstr(l):
    return ' '.join(map(str, l))


def llstr(ll):
    return '\n'.join(map(lstr, ll))


def main(n):
    # Define grid and step scales deterministically from n
    rows = max(1, n)
    cols = max(1, n)
    k = max(1, 2 * n)

    # Generate deterministic edge costs:
    # R: rows x (cols-1), C: (rows-1) x cols
    if cols > 1:
        R = [[(i + j + 1) % 9 + 1 for j in range(cols - 1)] for i in range(rows)]

    else:
        R = [[] for _ in range(rows)]

    if rows > 1:
        C = [[(i * cols + j + 1) % 9 + 1 for j in range(cols)] for i in range(rows - 1)]

    else:
        C = []

    G = explorer(rows, cols, k, R, C)
    if G:
        # print(llstr(G))
        pass

    else:
        s = ' '.join('-1' for _ in range(cols))
        # print('\n'.join(s for _ in range(rows)))
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)