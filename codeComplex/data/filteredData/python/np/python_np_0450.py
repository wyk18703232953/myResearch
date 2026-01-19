from array import array
from typing import Tuple


def solve_with_matrix(mat, n, m):
    bit = array('h', [1 << i for i in range(m)])
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = array('i', [-1]) * max_bit
        for i in range(n):
            mask = 0
            row = mat[i]
            for j in range(m):
                if row[j] >= x:
                    mask |= bit[j]
            dp[mask] = i

        for i in range(max_bit):
            if dp[i] == -1:
                continue
            for j in range(i, max_bit):
                if dp[j] != -1 and (i | j) == fullbit:
                    return dp[i], dp[j]

        return -1, -1

    ok, ng = 0, 10**9 + 1
    ans_i, ans_j = 1, 1

    while abs(ok - ng) > 1:
        mid = (ok + ng) >> 1
        x, y = solve(mid)
        if x == -1:
            ng = mid
        else:
            ok = mid
            ans_i, ans_j = x + 1, y + 1

    return ans_i, ans_j


def main(n: int):
    if n <= 0:
        print(1, 1)
        return

    # Define matrix dimensions based on n
    m = max(1, min(10, n))
    rows = max(1, n)

    # Deterministically generate matrix values
    # Value pattern is bounded to keep mid/binary search meaningful
    limit = 10**9
    mat = []
    for i in range(rows):
        row = []
        base = i * 131 + 7
        for j in range(m):
            val = (base + j * 97 + (i ^ j) * 31) % limit
            row.append(val)
        mat.append(array('i', row))

    ans_i, ans_j = solve_with_matrix(mat, rows, m)
    print(ans_i, ans_j)


if __name__ == "__main__":
    main(5)