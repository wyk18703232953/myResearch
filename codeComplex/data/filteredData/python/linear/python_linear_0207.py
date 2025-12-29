from __future__ import division
from collections import *
import random

def main(n):
    # 1. 生成测试数据
    # 随机生成一个安全间隔 s（0~59），以及 n 个时间点 (h, m)
    s = random.randint(0, 59)
    a = []
    for _ in range(n):
        h = random.randint(0, 23)  # 合理的小时范围
        m = random.randint(0, 59)
        a.append([h, m])

    # 2. 原逻辑：在 0<=i<26, 0<=j<60 中找一个时间 (i,j)
    # 使得与所有给定时间 (h,m) 在分钟线性空间上的距离（排除相邻1分钟）>= s
    ans = -1

    for i in range(26):
        for j in range(60):
            tem = i * 60 + j
            ans = (i, j)
            for h, m in a:
                tem2 = h * 60 + m
                if tem <= tem2:
                    if tem2 - (tem + 1) < s:
                        ans = -1
                        break
                else:
                    if tem - (tem2 + 1) < s:
                        ans = -1
                        break

            if ans != -1:
                print(f"{ans[0]} {ans[1]}")
                return

    # 如果没找到（原代码不会处理此情况），这里可以选择输出一个标记
    print("-1 -1")


if __name__ == "__main__":
    # 示例：规模 n 可以按需要调整
    main(5)