from math import *
from cmath import *
from itertools import *
from decimal import *
from fractions import *
from sys import *
from types import CodeType, new_class


def main(n):
    """
    n: 规模，用于生成测试数据
    功能：根据生成的 a, b 输出它们的公共元素（按 a 中出现的顺序）。
    """
    # 生成测试数据：
    # a 为 [0, 1, 2, ..., n-1]
    # b 为 [n//2, n//2+1, ..., 3*n//2-1]
    m = n  # 让 b 的长度与 a 相同
    a = list(range(n))
    b = list(range(n // 2, n // 2 + m))

    # 执行原逻辑：输出在 b 中也出现的那些 a 中元素
    b_set = set(b)  # 加速查找
    for x in a:
        if x in b_set:
            # print(x, end=' ')
            pass
if __name__ == "__main__":
    # 示例调用，可按需要修改或在外部调用 main(n)
    main(10)