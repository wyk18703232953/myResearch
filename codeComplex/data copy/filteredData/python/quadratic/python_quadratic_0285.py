from math import *
from cmath import *
from itertools import *
from decimal import *
from fractions import *
from sys import *
from types import CodeType, new_class


def main(n):
    # 输入结构：单组数据，两个整数 n, m；接着两行是长度为 n 和 m 的整数序列
    # 这里将参数 n 视为数组规模，将 m = n，生成两个长度为 n 的序列
    # 保持原逻辑：输出出现在 b 中的 a 中元素，按 a 的顺序，元素之间以空格分隔

    # 生成确定性的 n, m
    size_n = n
    size_m = n

    # 生成确定性的数组 a 和 b
    # a: 0, 1, 2, ..., n-1
    a = [i for i in range(size_n)]
    # b: (i * 2) % n for i in range(n)
    if size_m > 0:
        b = [(i * 2) % size_n for i in range(size_m)]

    else:
        b = []

    # 原始核心逻辑
    out = []
    for x in a:
        if x in b:
            out.append(str(x))
    if out:
        # print(" ".join(out))
        pass
if __name__ == "__main__":
    # 示例调用，可根据需要调整规模
    main(10)