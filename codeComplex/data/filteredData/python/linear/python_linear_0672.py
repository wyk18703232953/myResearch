#!/usr/bin/env python
# coding: utf-8

import random

def main(n):
    # 3. 根据 n 生成测试数据（示例：随机生成 n 个整数）
    # 你可以根据需要修改数据生成策略
    columns = [random.randint(0, 100) for _ in range(n)]

    # 原逻辑开始
    modcolumns = [i % 2 for i in columns]

    previouslist = []

    for i in range(n):
        if len(previouslist) == 0:
            previouslist.append(modcolumns[i])
        elif modcolumns[i] == previouslist[-1]:
            previouslist.pop()
        else:
            previouslist.append(modcolumns[i])

    if len(previouslist) <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：规模 n 可根据需要调整
    main(10)