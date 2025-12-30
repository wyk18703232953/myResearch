#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def main(n: int):
    """
    n 为规模参数，用于控制测试数据范围。
    这里根据 n 生成三整数 k1, k2, k3（1 <= ki <= n），
    然后复用原逻辑判断并输出结果。
    """

    # 生成测试数据：从 [1, n] 中随机取三个数
    k1 = random.randint(1, n)
    k2 = random.randint(1, n)
    k3 = random.randint(1, n)

    # 排序以复用原始代码逻辑
    k1, k2, k3 = sorted((k1, k2, k3))

    # 原始判定逻辑
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
    # 示例：可以在这里修改 n 的默认值，用于本地测试
    main(10)