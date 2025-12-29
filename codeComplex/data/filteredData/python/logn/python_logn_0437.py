# -*- coding:utf-8 -*-

import math
import random

# 预计算 f 数组
f = [0] * 100
for i in range(100):
    f[i] = (4 ** i - 1) // 3


def solve(N, K):
    if N < 100 and f[N] < K:
        print('NO')
        return

    for i in range(99):
        if f[i] <= K < f[i + 1]:
            x = K - f[i]
            a = N - i

            if x == 0:
                print('YES {}'.format(a))
                return

            edge = 2 ** (i + 1) - 1
            others = (2 ** i - 1) ** 2
            if edge == x:
                print('YES {}'.format(a - 1))
                return

            ans = a
            if edge < x:
                x -= edge
                ans = a - 1

            # split others
            for j in range(a + 1):
                if others * f[j] >= x:
                    print('YES {}'.format(ans))
                    return
            print('NO')
            return

    print('NO')


def main(n):
    """
    n 作为规模参数，用来控制测试数据大小。
    这里按如下方式生成测试数据：
      - T = n（测试组数）
      - 对于每组：
          N 在 [1, min(200, n+50)] 范围随机
          K 在 [0, min(10**12, 4**min(N, 60))] 范围随机
    """
    random.seed(0)
    T = n
    print(T)
    for _ in range(T):
        # 控制 N 的大小，避免过大导致 4**N 溢出或非常慢
        N = random.randint(1, min(200, n + 50))

        # 为了让 K 有一定分布，且不必严格与 f 对应，这里构造一个上界
        # 4**N 可能很大，因此对指数做截断
        exp = min(N, 60)
        maxK = min(10**12, (4 ** exp - 1) // 3 if exp >= 0 else 0)
        K = random.randint(0, maxK)

        print(N, K)
        solve(N, K)


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)