import sys
import collections
import math
import heapq
import bisect
from operator import itemgetter

def main(n):
    # 生成确定性输入：n, m, b 列表, g 列表
    if n <= 0:
        print(0)
        return

    # 将 n 拆分为两个部分，用于构造 b 和 g 的长度
    # 保证总规模与 n 线性相关且确定性
    len_b = max(1, n // 2)
    len_g = max(1, n - len_b)

    # b 中的数递增，保证较大的元素在后面
    b = [(i * 2 + 1) for i in range(len_b)]
    # g 中的数稍大一些，并在前部放一个较小值，保证有可行和不可行两种情况
    g = [(i * 2 + 2) for i in range(len_g)]
    if len_g > 0:
        g[0] = b[-1] if len_b > 0 else 0

    n_input = len_b
    m_input = len_g

    result = 0

    bMax, bMax2, bSum = -1, -1, 0
    for i, bb in enumerate(b):
        bSum += bb
        if bb > bMax:
            bMax2, bMax = bMax, bb
        elif bb > bMax2:
            bMax2 = bb

    gMin, gSum = float('inf'), 0
    for j, gg in enumerate(g):
        gSum += gg
        if gg < gMin:
            gMin = gg

    if bMax > gMin:
        result = -1
    else:
        result = bSum * m_input
        result += gSum
        result -= bMax * m_input
        if gMin > bMax:
            result += bMax - bMax2

    print(str(result))


if __name__ == "__main__":
    main(10)