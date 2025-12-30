# -*- coding:utf-8 -*-

import random

def main(n: int):
    """
    n 为规模参数，用来控制生成的测试数据范围。
    这里根据 n 生成 L, R，保证 L <= R，且数值大致在 [0, 2^min(n, 60)) 范围内。
    """
    # 生成测试数据
    max_bit = min(n, 60)  # 避免移位过大
    upper = 1 << max_bit if max_bit > 0 else 1
    L = random.randrange(0, upper)
    R = random.randrange(L, upper)  # 保证 L <= R

    # 原逻辑
    for i in range(64, -1, -1):
        if (L & (1 << i)) != (R & (1 << i)):
            print((1 << (i + 1)) - 1)
            return
    print(0)


if __name__ == "__main__":
    # 示例：调用 main，n 可按需要修改
    main(10)