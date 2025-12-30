#!/bin/python3

import random


def main(n: int):
    """
    n 作为规模参数，用来控制生成测试数据的大小范围。
    这里约定：
      - 随机生成 l, r，满足 0 <= l <= r <= 2^n - 1 （n 不宜过大，例如 <= 62）
    """
    if n <= 0:
        # 退化情况，统一输出 0
        print(0)
        return

    # 为避免位移过大，这里限制 n 最大为 62（与原代码一致）
    n_effective = min(n, 62)

    # 生成测试数据：0 <= l <= r <= 2^n_effective - 1
    max_val = (1 << n_effective) - 1
    l = random.randint(0, max_val)
    r = random.randint(l, max_val)

    # 原逻辑
    for i in range(62, -1, -1):
        if ((1 << i) & l) ^ ((1 << i) & r):
            print((1 << (i + 1)) - 1)
            break
    else:
        print(0)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)