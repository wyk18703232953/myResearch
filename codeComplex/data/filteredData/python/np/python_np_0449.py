import sys
from array import array
from typing import Tuple


def main(n: int) -> None:
    # Interpret n as the number of rows; fix m to a small constant
    m = 5
    if n <= 0:
        print(1, 1)
        return

    # Deterministically generate matrix of size n x m
    # mat[i][j] = (i * (j + 1) + j * j) % 100
    mat = [
        array('i', ((i * (j + 1) + j * j) % 100 for j in range(m)))
        for i in range(n)
    ]

    bit = [1 << i for i in range(m)]
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = array('i', [-1]) * max_bit
        for i in range(n):
            mask = 0
            row = mat[i]
            for j, y in enumerate(row):
                if y >= x:
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

    print(ans_i, ans_j)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)