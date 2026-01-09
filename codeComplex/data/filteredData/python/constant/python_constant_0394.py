import itertools
import bisect
import math
from collections import *
import os
import sys
from io import BytesIO, IOBase


def main(n):
    # 生成两个长度为 n 的只含 '0' 和 '1' 的字符列表
    a = [str((i * 37 + 3) % 2) for i in range(n)]
    b = [str((i * 91 + 7) % 2) for i in range(n)]

    a = list(a)
    b = list(b)
    ans = 0
    for i in range(n):
        if a[i] == "0":
            ans += 1
            if i - 1 >= 0 and a[i] == b[i] == b[i - 1]:
                a[i] = b[i] = b[i - 1] = "X"
            elif i + 1 < n and b[i] == b[i + 1] == a[i + 1] == a[i]:
                a[i] = b[i] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == b[i + 1]:
                a[i] = b[i] = b[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i + 1] == a[i + 1]:
                a[i] = b[i + 1] = a[i + 1] = "X"
            elif i + 1 < n and a[i] == b[i] == a[i + 1]:
                a[i] = b[i] = a[i + 1] = "X"

            else:
                ans -= 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)