#!/usr/bin/env python3
import random

def solve(n, k):
    if n == 1:
        print(0)
        return

    if n <= k:
        print(1)
        return

    lo, hi = 1, k - 1
    while lo < hi:
        mid = lo + (hi - lo + 1) // 2
        cum = (k - 2 + mid - 1) * (k - mid) // 2
        if cum < n - k:
            hi = mid - 1
        else:
            lo = mid

    if lo == 1:
        print(-1)
        return

    print(k - lo + 1)


def main(n):
    """
    n: problem规模，对应原程序中的 n。
    自动生成 k，并调用 solve(n, k)。
    """
    # 生成测试数据：约束 k >= 1
    # 令 k 在 [1, max(1, 2*n)] 之间随机选择
    k = random.randint(1, max(1, 2 * n))
    solve(n, k)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)