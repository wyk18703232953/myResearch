#!/usr/bin/env python
# coding: utf-8

import math

def main(n):
    if n <= 0:
        # print("YES")
        pass
        return

    # 确定性生成长度为 n 的整数列表
    columns = [(i * 3 + 1) for i in range(n)]

    modcolumns = [i % 2 for i in columns]

    test = 0
    previouslist = []

    for i in range(0, n):
        if len(previouslist) == 0:
            previouslist.append(modcolumns[i])
        elif modcolumns[i] == previouslist[-1]:
            previouslist.pop()

        else:
            previouslist.append(modcolumns[i])

    if len(previouslist) <= 1:
        # print("YES")
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)