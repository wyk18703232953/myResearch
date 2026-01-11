import os
import sys
from math import *
from collections import *
from bisect import *
from io import BytesIO, IOBase

ALPHA = "abcdefghijklmnopqrstuvwxyz/"
M = 1000000007
EPS = 1e-6


def Ceil(a, b):
    return a // b + int(a % b > 0)


def main(n):
    a = [i % 10 for i in range(n)]
    dic = defaultdict(lambda: 0)
    cursum = 0
    ans = 0
    for i in range(n):
        ele = a[i]
        if ele - 1 in dic.keys() and ele + 1 in dic.keys():
            ans += ele * (i - dic[ele - 1] - dic[ele + 1]) - (
                cursum - (dic[ele - 1] * (ele - 1) + dic[ele + 1] * (ele + 1))
            )
        elif ele - 1 in dic.keys():
            ans += ele * (i - dic[ele - 1]) - (cursum - (dic[ele - 1] * (ele - 1)))
        elif ele + 1 in dic.keys():
            ans += ele * (i - dic[ele + 1]) - (cursum - (dic[ele + 1] * (ele + 1)))

        else:
            ans += ele * i - cursum
        dic[ele] += 1
        cursum += ele
    # print(ans)
    pass
if __name__ == "__main__":
    main(10_000)