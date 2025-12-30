from collections import deque, defaultdict, Counter
from itertools import product, groupby, permutations, combinations
from math import gcd, floor, inf, log2, sqrt, log10
from bisect import bisect_right, bisect_left
from statistics import mode
from string import ascii_uppercase
import random


def digit_at_position(k: int) -> str:
    """
    原逻辑提取为函数：
    返回无限串 "12345678910111213..." 中第 k(0-based) 个字符
    """
    # 原代码中：k = int(input()) - 1
    k -= 1

    y = 9
    x = 1
    while k > x * y:
        k -= x * y
        y *= 10
        x += 1

    start = 10 ** (x - 1)
    start += k // x

    return str(start)[k % x]


def main(n: int):
    """
    n 为规模参数，用于生成测试数据：
    - 生成 1..n 的所有 k，依次输出对应的第 k 个字符。
    """
    # 示例：生成从 1 到 n 的测试 k
    ks = list(range(1, n + 1))

    # 对每个 k 调用 digit_at_position 并打印结果
    for k in ks:
        print(digit_at_position(k))


if __name__ == "__main__":
    # 示例调用，可自行修改或在外部调用 main(n)
    main(10)