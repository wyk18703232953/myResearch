# -*- coding:utf-8 -*-

import random

def main(n: int):
    """
    n: 规模参数，用于控制测试数据范围
       本题需要两个整数 L, R，且 L <= R。
       我们用 n 来控制它们的最大值：0 <= L <= R <= max_val，其中 max_val = 2**min(n, 63) - 1
    """
    # 1. 根据 n 生成测试数据
    # 为避免位移超过64位，这里把上界限制在 2**63-1
    bit_limit = min(n, 63)
    max_val = (1 << bit_limit) - 1 if bit_limit > 0 else 0

    if max_val == 0:
        L = 0
        R = 0
    else:
        L = random.randint(0, max_val)
        R = random.randint(L, max_val)

    # 2. 原逻辑：在 [L,R] 范围内，求能得到的最大异或值
    for i in range(64, -1, -1):
        if (L & (1 << i)) != (R & (1 << i)):
            print((1 << (i + 1)) - 1)
            return
    print(0)


if __name__ == "__main__":
    # 示例调用：可以修改这里的 n 来控制生成数据的规模
    main(10)