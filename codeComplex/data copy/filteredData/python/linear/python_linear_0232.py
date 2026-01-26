import sys
from math import *
from collections import *
from bisect import *

ALPHA = "abcdefghijklmnopqrstuvwxyz/"
M = 1000000007
EPS = 1e-6


def Ceil(a, b):
    return a // b + int(a % b > 0)


def main(n):
    # 生成长度为 n 的字符串 s，周期为 5 的确定性模式
    pattern = "abxxc"
    s = "".join(pattern[i % len(pattern)] for i in range(n))

    ans = 0
    cnt = 0
    for x in s:
        if x == "x":
            cnt += 1
            if cnt >= 3:
                ans += 1

        else:
            cnt = 0
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)