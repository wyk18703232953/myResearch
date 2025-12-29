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
    n: 问题规模，用于生成测试数据中的 n, k。
    这里将原算法中的 n 设置为 n，
    k 随机生成在 [1, n] 范围内，且保证 k >= 1。
    可根据需要自行调整生成规则。
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    # 生成测试数据
    N = n
    K = random.randint(1, max(1, n))

    # 执行原逻辑
    solve(N, K)


if __name__ == "__main__":
    # 示例：调用 main，规模可调整
    main(10)