import sys
from math import sqrt, log, log2, ceil, log10, gcd, floor, pow, sin, cos, tan, pi, inf, factorial
from copy import copy, deepcopy
from sys import exit, stdin, stdout
from collections import Counter, defaultdict, deque
from itertools import permutations
import heapq
from bisect import bisect_left 
from bisect import bisect_right

mod = 1000000007

def solve(n, s, data):
    cm = 0
    for i in range(n):
        fi, ti = data[i]
        if i == 0:
            cm = fi + ti

        else:
            if fi + ti > cm:
                cm = fi + ti
    if cm > s:
        return cm

    else:
        return s

def main(n):
    # 将 n 作为输入规模：n 为 (n, s) 中的 n，同时生成 n 组 (fi, ti)
    # 确定性生成 s
    s = n * 3  # 例：s 随 n 线性增长

    # 确定性生成 n 组 (fi, ti)
    # 示例构造：fi = i，ti = (2*i) % (n+1)
    data = [(i, (2 * i) % (n + 1)) for i in range(n)]

    # 保持原逻辑：单测试用例
    result = solve(n, s, data)
    # print(result)
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)