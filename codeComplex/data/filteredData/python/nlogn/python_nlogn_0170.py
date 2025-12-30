#!/usr/bin/env python
# coding=utf-8

import random

def main(n):
    # 1. 生成测试数据：n 对 (x, y)
    # 可根据需要调整生成范围
    xy_pairs = []
    for _ in range(n):
        x = random.randint(-10**9, 10**9)
        y = random.randint(-10**9, 10**9)
        xy_pairs.append((x, y))

    # 2. 原始逻辑：将 (x, y) 转换为 (x + y, x - y)
    l = []
    for x, y in xy_pairs:
        l.append((x + y, x - y))

    # 3. 排序
    l.sort()

    # 4. 计算答案
    r = -2000000000
    a = 0
    for u in l:
        if u[1] >= r:
            a += 1
            r = u[0]

    # 5. 输出结果
    print(a)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)

# Made By Mostafa_Khaled