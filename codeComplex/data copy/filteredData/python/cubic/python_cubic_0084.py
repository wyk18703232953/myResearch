import sys
from array import array

mod = 10**9 + 7


def build_edge(n):
    # Deterministic generation of an n x n 0/1 matrix
    # edge[i][j] = 1 if i < j and (i + j) is even, else 0
    edge = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            edge[i][j] = 1 if (i + j) % 2 == 0 else 0
    return edge


def run_algorithm(edge):
    n = len(edge)
    dp_f = [array('i', [-1]) * n for _ in range(n)]
    dp_g = [array('i', [-1]) * n for _ in range(n)]

    for i in range(n):
        dp_f[i][i] = 1
        dp_g[i][i] = 1
    for i in range(n - 1):
        dp_f[i][i + 1] = 1 if edge[i][i + 1] else 0
        dp_g[i][i + 1] = 1 if edge[i][i + 1] else 0

    def f(l, r):
        if dp_f[l][r] != -1:
            return dp_f[l][r]

        if edge[l][r]:
            dp_f[l][r] = g(l, r)

        else:
            dp_f[l][r] = 0

        for m in range(l + 1, r):
            if edge[l][m]:
                dp_f[l][r] = (dp_f[l][r] + g(l, m) * f(m, r)) % mod

        return dp_f[l][r]

    def g(l, r):
        if dp_g[l][r] != -1:
            return dp_g[l][r]

        dp_g[l][r] = f(l + 1, r)
        for m in range(l + 1, r):
            dp_g[l][r] = (dp_g[l][r] + f(l, m) * f(m + 1, r)) % mod

        return dp_g[l][r]

    return f(0, n - 1) if n > 0 else 0


def main(n):
    edge = build_edge(n)
    result = run_algorithm(edge)
    # print(result)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(5)