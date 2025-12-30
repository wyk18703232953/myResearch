#!/bin/python3

import random

def main(n):
    """
    n: 控制测试数据规模，例如最大数值范围 [0, 2^n - 1]
    """
    if n <= 0:
        l, r = 0, 0
    else:
        max_val = (1 << n) - 1
        l = random.randint(0, max_val)
        r = random.randint(0, max_val)
        if l > r:
            l, r = r, l

    # 原逻辑：求 l 和 r 之间的最大异或值
    for i in range(62, -1, -1):
        if ((1 << i) & l) ^ ((1 << i) & r):  # if xor of max bit is 1
            print((1 << (i + 1)) - 1)
            break
    else:
        print(0)


if __name__ == "__main__":
    # 示例：可根据需要修改 n
    main(10)