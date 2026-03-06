from array import array
from typing import Tuple


def main(n: int):
    # Interpret n as number of rows; number of columns m kept small and fixed
    # to keep complexity dominated by n for scaling experiments.
    m = 10

    # Deterministic matrix generation: values increase with i, j
    # so that there is a non-trivial distribution for the binary search.
    mat = [array('i', [(i * m + j) % 1000 for j in range(m)]) for i in range(n)]

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

    print(ans_i, ans_j)


if __name__ == "__main__":
    main(1000)