import os
import sys
from math import *
from collections import *
from heapq import *
from bisect import *
from io import BytesIO, IOBase

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def Ceil(a, b):
    return a // b + int(a % b > 0)

def main(n):
    # 生成确定性的 (n, k)
    # 约束: n >= 1, 1 <= k <= n, 且 (n-k) 为偶数 (否则原逻辑 (n-k)//2 不一定覆盖所有情况)
    if n < 1:
        n = 1
    k = n if n % 2 == 1 else n - 1  # 保证 n-k 为偶数且 k>=1
    if k < 1:
        k = 1
    if k > n:
        k = n

    rep = [1] + [0] * ((n - k) // 2)
    cur = 0

    ans = []
    j = 0
    for i in range(n):
        ans.append(rep[j])
        j = (j + 1) % len(rep)

    if k == 1:
        ans = [1] + [0] * (n - 1)

    # 输出与原程序格式一致的结果
    # print(*ans, sep='')
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以做规模实验
    main(10)