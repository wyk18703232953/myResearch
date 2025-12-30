import sys
import math
import random
import collections
import bisect

sys.setrecursionlimit(1000000)


def main(n):
    """
    n: 规模，用来生成测试数据
    逻辑对应原程序：
    输入:
        N, M
        N 个整数 za
    """
    # 1. 根据 n 生成测试数据
    # 这里选取：
    #   N = n
    #   M = 0（原代码中未使用 M）
    #   za 为长度为 N 的整数数组，值在 [1, n] 范围内
    N = n
    M = 0
    random.seed(1)
    za = [random.randint(1, max(1, n)) for _ in range(N)]

    # 2. 原逻辑开始
    za.sort(reverse=True)

    re = 0

    for i in range(N - 1):
        a = za[i]
        b = za[i + 1]
        g = b
        if g >= a:
            t = a - 1
            if t < 1:
                t = 1
            re += g - t
            za[i + 1] = t
            re += a - 1
        else:
            re += g

    print(re)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)