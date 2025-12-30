# -*- coding: utf-8 -*-
"""
Converted to parameterized main(n) without input().
Original logic:
- Read l, r
- Compute x = l ^ r
- If x != 0:
    k = floor(log2(x))
    ans = (1 << (k + 1)) - 1
  else:
    ans = 0
"""

import math
import random


def main(n):
    """
    n: controls the scale of generated test data.
       Here we generate two non-negative integers l, r with bit-length up to n.
    """
    # 1. 生成测试数据 (l, r)，数值规模受 n 控制
    if n <= 0:
        # 退化情形，直接固定为 0, 0
        l, r = 0, 0
    else:
        # 生成位数不超过 n 的随机非负整数
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)

    # 2. 原始逻辑：根据 l, r 计算结果
    x = l ^ r
    if x:
        k = int(math.log(x, 2))
        ans = (1 << (k + 1)) - 1
    else:
        ans = 0

    # 3. 输出结果（可根据需要调整输出形式）
    print(ans)


if __name__ == "__main__":
    # 示例：以 n = 10 规模运行一次
    main(10)