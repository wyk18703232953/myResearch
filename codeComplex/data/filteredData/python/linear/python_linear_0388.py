import time
from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def main(n):
    # 映射：n 为原程序中的 n，m 也取为 n，使输入规模随 n 线性增长
    orig_n = n
    m = n

    # 确定性生成 X, D
    # X: 1, 2, ..., m
    # D: 对称的正负模式
    X = [i + 1 for i in range(m)]
    D = [((i % 4) - 1) * ((-1) ** i) for i in range(m)]

    summ = orig_n * sum(X)

    for i in range(m):
        d = D[i]
        if d < 0:
            if orig_n % 2 == 1:
                summ += d * (orig_n // 2) * (orig_n // 2 + 1)

            else:
                summ += d * (orig_n // 2) * (orig_n // 2)

        else:
            summ += d * (orig_n - 1) * orig_n // 2

    # print(summ / orig_n)
    pass
if __name__ == "__main__":
    main(10)