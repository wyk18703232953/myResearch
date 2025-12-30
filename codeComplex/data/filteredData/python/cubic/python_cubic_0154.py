from functools import lru_cache
from collections import defaultdict
import random


def solve(N, A):
    # Alternative solution O(N^3) DP
    def tup(l, r):
        return l * 16384 + r

    def untup(t):
        return divmod(t, 16384)

    cache = {}

    def f(lr):
        if lr not in cache:
            l, r = untup(lr)
            # l inclusive, r exclusive
            # Returns (length, val) where length is min length and val is the sole value when length is one
            if r - l == 1:
                return tup(1, A[l])
            best = tup(float("inf"), float("inf"))
            for i in range(l + 1, r):
                # Try every split
                lSplit = f(tup(l, i))
                rSplit = f(tup(i, r))
                lLen, lVal = untup(lSplit)
                rLen, rVal = untup(rSplit)
                if lLen != 1 or rLen != 1:
                    # If either can't be merged down to one, just add the length of each
                    best = min(best, tup(lLen + rLen, 9999))
                else:
                    if lVal == rVal:
                        # Both same, can merge into length 1 with val + 1
                        best = min(best, tup(1, lVal + 1))
                    else:
                        # Different, forms a new array of length 2
                        best = min(best, tup(2, 9999))
            cache[lr] = best

        return cache[lr]

    ans = untup(f(tup(0, N)))[0]
    return ans


def main(n):
    # 根据规模 n 生成测试数据
    # A[i] 在 0~1000 范围内
    random.seed(0)
    N = n
    A = [random.randint(0, 1000) for _ in range(N)]
    ans = solve(N, A)
    print(ans)


if __name__ == "__main__":
    # 示例：使用 n = 10 运行
    main(10)