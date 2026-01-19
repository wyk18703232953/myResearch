import sys
from array import array
from typing import Tuple


def main(n: int) -> None:
    # Interpret n as number of rows; derive number of columns deterministically
    if n <= 0:
        return
    m = max(1, n // 2)

    # Deterministically construct a matrix mat of size n x m with integer values
    mat = []
    for i in range(n):
        row = []
        for j in range(m):
            # Simple deterministic arithmetic pattern
            row.append((i * m + j) % 1000)
        mat.append(array('i', row))

    bit = [1 << i for i in range(m)]
    fullbit = (1 << m) - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = {sum(bit[j] for j, y in enumerate(mat[i]) if y >= x): i for i in range(n)}
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
    # Example deterministic call; adjust n for different input scales
    main(10)