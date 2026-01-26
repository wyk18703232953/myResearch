from collections import deque
from collections import OrderedDict
import math
import sys
import os
import threading
import bisect
import operator
import heapq
from atexit import register
from io import BytesIO
import io


def main(n):
    # 映射规则：
    # n 控制 r, g, b 的大小，分别为:
    # r = n
    # g = max(1, n // 2)
    # b = max(1, n // 3)
    # 并且都不超过 200（因为 dp 数组是 205^3）
    max_size = 200
    r = min(n, max_size)
    g = min(max(1, n // 2), max_size)
    b = min(max(1, n // 3), max_size)

    # 生成三种颜色的数组，每个长度分别为 r, g, b
    # 使用简单的算术构造，保证确定性
    a = []
    a0 = [(i * 2 + 3) % 1000 + 1 for i in range(r)]
    a1 = [(i * 3 + 5) % 1000 + 1 for i in range(g)]
    a2 = [(i * 5 + 7) % 1000 + 1 for i in range(b)]
    a.append(sorted(a0, reverse=True))
    a.append(sorted(a1, reverse=True))
    a.append(sorted(a2, reverse=True))

    # DP 部分保持原始算法逻辑
    max_dim = 205
    dp = [[[0 for _ in range(max_dim)] for _ in range(max_dim)] for _ in range(max_dim)]
    answer = 0

    for i in range(r + 1):
        for j in range(g + 1):
            for k in range(b + 1):
                if i < r and j < g:
                    val = dp[i][j][k] + a[0][i] * a[1][j]
                    if val > dp[i + 1][j + 1][k]:
                        dp[i + 1][j + 1][k] = val
                if i < r and k < b:
                    val = dp[i][j][k] + a[0][i] * a[2][k]
                    if val > dp[i + 1][j][k + 1]:
                        dp[i + 1][j][k + 1] = val
                if j < g and k < b:
                    val = dp[i][j][k] + a[1][j] * a[2][k]
                    if val > dp[i][j + 1][k + 1]:
                        dp[i][j + 1][k + 1] = val
                if dp[i][j][k] > answer:
                    answer = dp[i][j][k]

    # 下面这部分保持原程序结构，但使用确定性数据，不依赖输入
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    p1 = Person("heelo", 27)

    # 将 help 输出替换为简单的确定性属性访问结果，避免交互式帮助系统输出
    person_info = (p1.name, p1.age)

    age = 26
    name = 'Swaroop'
    formatted_str = 'Возрас {} -- {} лет'.format(name, age)

    # 对 object 的 help 同样避免真实 help 调用，保持确定性与可控输出规模
    object_info = ("object_base",)

    # 返回一个汇总结果，包含 DP answer 和一些确定性派生值
    return {
        "r": r,
        "g": g,
        "b": b,
        "dp_answer": answer,
        "person_info": person_info,
        "formatted_str": formatted_str,
        "object_info": object_info,
    }


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    result = main(10)
    # 为了和原程序一样有输出，这里仅输出 DP 的核心结果
    # print(result["dp_answer"])
    pass