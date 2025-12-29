#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def main(n: int):
    """
    n 用作规模参数，这里用于控制生成测试数据的范围：
    1 <= k_i <= max(5, n)
    生成一组三个整数 (k1, k2, k3)，代替原来的 input().
    """
    upper = max(5, n)
    # 根据 n 生成测试数据
    k1 = random.randint(1, upper)
    k2 = random.randint(1, upper)
    k3 = random.randint(1, upper)

    # 原始逻辑
    k1, k2, k3 = sorted((k1, k2, k3))

    if (
        1 == k1
        or (2 == k1 and 2 == k2)
        or (3 == k1 and 3 == k2 and 3 == k3)
        or (k1 == 2 and k2 == 4 and k3 == 4)
    ):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main，规模参数可按需修改
    main(10)