import sys
from array import array  # noqa: F401
from typing import List, Tuple, TypeVar, Generic, Sequence, Union  # noqa: F401


def solve(i, n, delta, delta2):
    inf = 2 * 10**9
    dp = [[-1] * n for _ in range(1 << n)]
    dp[(1 << i)][i] = inf
    stack = [(1 << i, i)]

    for t in range(1, n + 1):
        next_s = []
        for bit, v in stack:
            for dest in range(n):
                if (1 << dest) & bit:
                    continue
                if dp[bit | (1 << dest)][dest] == -1:
                    next_s.append((bit | (1 << dest), dest))
                dp[bit | (1 << dest)][dest] = max(dp[bit | (1 << dest)][dest], min(dp[bit][v], delta[v][dest]))

        stack = next_s

    return max(min(delta2[j][i], dp[-1][j]) for j in range(n) if i != j)


def generate_matrix(n: int, m: int):
    # deterministic integer matrix generation depending only on n and m
    return [tuple((i * m + j) % (2 * 10**9) for j in range(m)) for i in range(n)]


def main(n: int):
    # interpret n as the number of rows; derive a deterministic number of columns
    if n <= 0:
        return
    m = max(2, (n % 7) + 2)

    matrix = generate_matrix(n, m)

    if n == 1:
        print(min(abs(x - y) for x, y in zip(matrix[0], matrix[0][1:])))
        return

    delta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            delta[i][j] = delta[j][i] = min(abs(x - y) for x, y in zip(matrix[i], matrix[j]))
    delta2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            delta2[i][j] = min((abs(x - y) for x, y in zip(matrix[i], matrix[j][1:])), default=2 * 10**9)

    print(max(solve(i, n, delta, delta2) for i in range(n)))


if __name__ == "__main__":
    # example deterministic call for time complexity experiments
    main(5)