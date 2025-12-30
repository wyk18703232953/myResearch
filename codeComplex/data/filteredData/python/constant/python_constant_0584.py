from bisect import bisect_right as br
from bisect import bisect_left as bl
from math import *
import random

def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True

def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)

def main(n):
    # 生成测试数据：在 [1, n] 内随机选取 (a, b)
    if n < 1:
        return
    a = random.randint(1, n)
    b = random.randint(1, n)

    if mhd(a, b, 1, 1) <= mhd(a, b, n, n):
        print('White')
    else:
        print('Black')

if __name__ == "__main__":
    # 示例：调用 main，规模可自行调整
    main(8)