import sys
import math
import bisect
import collections
import atexit

sys.setrecursionlimit(1000000)

def dprint(*args, **kwargs):
    pass

def main(n):
    # n 作为数组长度
    if n <= 0:
        return
    # 确定性生成长度为 n 的整数数组 za
    # 构造一个含正负混合的序列，避免总是走同一分支
    za = [((i * 2 - n) // 3) for i in range(n)]
    N = n

    if N == 1:
        print(za[0])
        return
    t1 = max(za)
    t2 = min(za)
    if t2 >= 0:
        print(sum(za) - 2 * t2)
        return
    if t1 <= 0:
        print(2 * t1 - sum(za))
        return

    res = 0
    for x in za:
        res += abs(x)
    print(res)

if __name__ == "__main__":
    main(10)