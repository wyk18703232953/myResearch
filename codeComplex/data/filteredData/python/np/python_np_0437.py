import os
import sys
from io import BytesIO, IOBase


def solve(n, m, a):
    ans = []
    le = 0
    ri = int(1e9)

    def check(mid: int) -> bool:
        nonlocal ans
        dic = {}
        for i in range(n):
            bit = 0
            for j in range(m):
                if a[i][j] >= mid:
                    bit += 1
                bit <<= 1
            dic[bit >> 1] = i
        for x, idx in dic.items():
            for y, idy in dic.items():
                if x | y == 2 ** m - 1:
                    ans = idx + 1, idy + 1
                    return True
        return False

    while le <= ri:
        mid = (le + ri) >> 1
        if check(mid):
            le = mid + 1
        else:
            ri = mid - 1
    return ans


def main(n):
    m = n
    a = [[(i + 1) * (j + 2) % (10 ** 9 + 7) for j in range(m)] for i in range(n)]
    ans = solve(n, m, a)
    if ans:
        print(ans[0], ans[1])
    else:
        print(-1, -1)


if __name__ == "__main__":
    main(5)