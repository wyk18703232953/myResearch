import math
import random
from collections import Counter, defaultdict
from bisect import bisect_right, bisect_left, insort_right
from heapq import heappop, heappush
from itertools import accumulate
from sys import stdout


def main(n):
    """
    n: 规模参数，用于生成测试数据的长度。
    逻辑保持与原程序一致：
      t: 由'+'和'-'组成的长度为 n 的字符串
      s: 由'+'、'-'和'?'组成的长度为 n 的字符串
    """

    # 生成测试数据：
    # t 只含 '+' 和 '-'
    t_chars = ['+', '-']
    t = ''.join(random.choice(t_chars) for _ in range(n))

    # s 含 '+', '-', '?'
    s_chars = ['+', '-', '?']
    s = ''.join(random.choice(s_chars) for _ in range(n))

    # 原逻辑
    k = t.count('+') - s.count('+')
    unknown = s.count('?')

    if k > unknown or k < 0:
        print('0.0')
    else:
        res = (
            math.factorial(unknown)
            / (math.factorial(k) * math.factorial(unknown - k))
            / (2 ** unknown)
        )
        print(res)


if __name__ == "__main__":
    # 可以在此处修改 n 来测试
    main(10)