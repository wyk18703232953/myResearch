#------------------------template--------------------------#
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

#-------------------------code---------------------------#

def main(n):
    """
    生成测试数据并执行原逻辑。
    这里将规模参数 n 用作原程序中的 n，
    并构造一个合理的 k（1 <= k <= n, 且 (n-k) 为偶数以满足原表达式 (n-k)//2 的语义）。
    """
    # 构造测试数据：
    # 为保证 (n - k) >= 0 且为偶数，这里选择：
    # 若 n 为偶数，则 k = n
    # 若 n 为奇数，则 k = n - 1
    if n <= 0:
        return ""  # 对非法规模返回空字符串

    if n % 2 == 0:
        k = n

    else:
        k = n - 1  # 保证 n-k 为偶数且 >= 0

    # 原始逻辑开始（移除了 input，直接使用 n, k）

    rep = [1] + [0] * ((n - k) // 2)
    cur = 0

    ans = []
    j = 0
    for i in range(n):
        ans.append(rep[j])
        j = (j + 1) % len(rep)

    if k == 1:
        ans = [1] + [0] * (n - 1)

    # 原程序是直接打印，这里返回字符串结果方便外部使用
    output = ''.join(str(x) for x in ans)
    # print(output)
    pass
    return output


if __name__ == "__main__":
    # 示例：调用 main，规模可自行修改
    main(10)