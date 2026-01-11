import math
import collections
import bisect
import time
from itertools import permutations

def main(n):
    if n <= 0:
        return
    # 构造长度为 n 的数组，元素为 i 的线性组合，保证可重复且有一定分布
    arr = [(i * 3 + 5) for i in range(n)]
    unique = set(arr)
    poss = False

    # 保留原逻辑：优先寻找长度为 3 的符合条件的序列
    for i in arr:
        for j in range(32):
            val_plus = i + (1 << j)
            val_minus = i - (1 << j)
            if val_plus in unique and val_minus in unique:
                # print(3)
                pass
                # print(i, val_plus, val_minus)
                pass
                poss = True
                break
        if poss:
            break

    if poss:
        return

    # 其次寻找长度为 2 的符合条件的序列
    for i in arr:
        for j in range(32):
            val_plus = i + (1 << j)
            if val_plus in unique:
                # print(2)
                pass
                # print(i, val_plus)
                pass
                poss = True
                break
        if poss:
            break

    if poss:
        return

    # 否则输出单个元素
    # print(1)
    pass
    # print(arr[0])
    pass
if __name__ == "__main__":
    main(10)