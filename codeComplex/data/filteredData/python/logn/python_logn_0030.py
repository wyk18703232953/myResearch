import math
import sys
from decimal import Decimal
import random


def solve(l, r):
    if l == r:
        return 0

    val = 1
    while val * 2 <= r:
        val *= 2

    if val <= l:
        return solve(l - val, r - val)
    else:
        return 2 * val - 1


def main(n):
    # 生成测试数据：根据规模 n 生成 l, r
    # 这里将 r 设为 [1, 2^k] 范围内的随机数，l 为 [0, r] 内随机数
    # n 控制最大 2^k 的大小
    if n < 1:
        n = 1
    max_val = 2 ** n
    r = random.randint(1, max_val)
    l = random.randint(0, r)
    result = solve(l, r)
    print(result)


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的值
    main(10)