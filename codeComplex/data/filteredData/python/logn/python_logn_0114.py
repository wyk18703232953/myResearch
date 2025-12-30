#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import random


def solve(l, r):
    n = len(bin(r)[2:])
    ans = 0
    for x in range(0, n + 1):
        if ((r >> x) & 1) == 1 and ((l >> x) & 1) == 0:
            ans = max(ans, (1 << x) ^ ((1 << x) - 1))
    return ans


def main(n):
    """
    n 为规模参数，用于生成测试数据。
    这里根据 n 生成 [l, r]：
      - 取一个随机 bit 长度 b（1 <= b <= n）
      - 在该 bit 长度范围内随机生成 l, r，并保证 l <= r
    """
    random.seed(0)
    b = max(1, n)
    # r 至多为 2^b - 1，但避免过大整数，这里限制 b 不超过 60
    b = min(b, 60)
    max_val = (1 << b) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)
    ans = solve(l, r)
    print(ans)


# -----------------------------BOSS-------------------------------------!
# region fastio


# endregion

if __name__ == "__main__":
    # 示例：使用 n=10 调用
    main(10)