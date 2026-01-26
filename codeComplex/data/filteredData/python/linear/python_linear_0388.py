import time
from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque
from collections import Counter


def main(n):
    # 映射规则：
    # n: 原程序中的 n
    # m: 原程序中的 m（这里设为 n）
    # X, D 长度均为 m
    m = n
    if n <= 0:
        # print(0)
        pass
        return

    # 确定性生成 X 和 D
    # X[i] = i + 1
    # D[i]: 正负交替，幅度与索引相关
    X = [i + 1 for i in range(m)]
    D = [((1 if i % 2 == 0 else -1) * (i + 1)) for i in range(m)]

    summ = n * sum(X)

    for i in range(m):
        d = D[i]
        if d < 0:
            if n % 2 == 1:
                summ += d * (n // 2) * (n // 2 + 1)

            else:
                summ += d * (n // 2) * (n // 2)

        else:
            summ += d * (n - 1) * n // 2

    # print(summ / n)
    pass
if __name__ == "__main__":
    main(10)