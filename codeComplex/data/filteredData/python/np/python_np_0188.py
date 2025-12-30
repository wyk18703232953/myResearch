# -*- coding: utf-8 -*-

import random

def main(n):
    """
    n: 规模参数，用于生成测试数据
    约定：
      - N = n
      - L, H, d 以及数组 l 随机生成
    """
    # 1. 生成测试数据
    N = n
    if N <= 0:
        print(0)
        return

    # 生成参数范围可按需要调整
    # 为了保证有意义的区间，先生成数组，再设定 L, H
    l = [random.randint(1, 100) for _ in range(N)]
    total_sum = sum(l)

    # 随机生成 L, H，保证 L <= H，且在 [0, total_sum] 范围内
    L = random.randint(0, total_sum)
    H = random.randint(L, total_sum)

    # d 在一个适当范围内
    d = random.randint(0, max(l) - min(l) if N > 1 else 0)

    # 2. 原逻辑部分
    e = 0
    for i in range(1 << N):
        k = []
        for j in range(N):
            if (i >> j) & 1:
                k.append(l[j])
        if k:
            maz = max(k)
            mins = min(k)
            sums = sum(k)
            if L <= sums <= H:
                if maz - mins >= d:
                    e += 1

    print(e)


if __name__ == "__main__":
    # 可在此修改 n 进行测试
    main(5)