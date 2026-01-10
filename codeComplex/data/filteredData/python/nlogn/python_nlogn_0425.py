import os
import sys
from math import *
from collections import *
from bisect import *
from io import BytesIO, IOBase

ALPHA = 'abcdefghijklmnopqrstuvwxyz'
M = 998244353
EPS = 1e-6

def Ceil(a, b):
    return a // b + int(a % b > 0)

BUFSIZE = 8192

def main(n):
    # 确定性数据生成：长度为 n 的数组，元素为 i % (2*n+1)
    a = [i % (2 * n + 1) for i in range(n)]
    C = Counter(a)
    a_set = set(a)

    ans = 0

    for x in a_set:
        ok = True
        for i in range(65):
            need = (1 << i) - x
            if need == x and C[need] > 1:
                ok = False
                break
            if need != x and C[need] > 0:
                ok = False
                break
        if ok:
            ans += C[x]

    print(ans)

if __name__ == "__main__":
    main(10)