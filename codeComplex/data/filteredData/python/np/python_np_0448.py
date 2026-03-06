from array import array
from typing import Tuple


def main(n: int):
    # Interpret n as both number of rows and columns
    if n <= 0:
        print(1, 1)
        return

    N = n
    M = n

    # Deterministically generate matrix mat of size N x M
    # mat[i][j] = (i * 131 + j * 137) % (10**9 + 7)
    MOD = 10**9 + 7
    mat = [
        array('i', ((i * 131 + j * 137) % MOD for j in range(M)))
        for i in range(N)
    ]

    bit = [1 << i for i in range(M)]
    fullbit = (1 << M) - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = {
            sum(bit[j] for j, y in enumerate(mat[i]) if y >= x): i
            for i in range(N)
        }
        keys = tuple(dp.keys())

        for i in range(len(keys)):
            for j in range(i, len(keys)):
                if keys[i] | keys[j] == fullbit:
                    return dp[keys[i]], dp[keys[j]]

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
    main(5)