import sys
from array import array  # noqa: F401
from typing import Dict, List, Tuple, TypeVar, Generic, Sequence, Union  # noqa: F401


def input():
    return sys.stdin.buffer.readline().decode('utf-8')


def main():
    n, m = map(int, input().split())
    mat = [array('i', map(int, input().split())) for _ in range(n)]
    bit = [1 << i for i in range(m)]
    max_bit = 1 << m
    fullbit = max_bit - 1

    def solve(x: int) -> Tuple[int, int]:
        dp = array('i', [-1]) * max_bit
        for i in range(n):
            dp[sum(bit[j] for j, y in enumerate(mat[i]) if y >= x)] = i

        for i in range(max_bit):
            if dp[i] == -1:
                continue
            for j in range(i, max_bit):
                if dp[j] != -1 and i | j == fullbit:
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


if __name__ == '__main__':
    main()
