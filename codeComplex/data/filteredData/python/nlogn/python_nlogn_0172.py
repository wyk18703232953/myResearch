# -*- coding: utf-8 -*-
"""
原程序功能说明（推断）：
给定 n 个区间中心与半径 (k, m)，相当于区间 [k - m, k + m]。
程序按 k + m 升序排序后，贪心选择相互不相交的区间个数。

本版本：
1. 去掉 input()。
2. 封装为 main(n)。
3. 根据 n 随机生成测试数据 (k, m)，并返回答案。
"""

import random


def generate_test_data(n, k_range=(-10**6, 10**6), m_range=(0, 10**6)):
    """
    生成 n 个 (k, m) 对：
    k 在 k_range 内随机整数
    m 在 m_range 内随机整数
    """
    l = []
    for _ in range(n):
        k = random.randint(*k_range)
        m = random.randint(*m_range)
        l.append((k, m))
    return l


def solve_interval_selection(l):
    """
    给定 (k, m) 列表，求最大数量的互不相交“区间”个数。
    区间定义为中心 k、半径 m，对应区间 [k - m, k + m]。
    按 k + m 排序，然后贪心选择。
    """
    n = len(l)
    if n == 0:
        return 0

    # 按右端点 k + m 升序排序
    l.sort(key=lambda x: x[0] + x[1])

    last = 0
    ans = 1
    for i in range(1, n):
        # 若两个区间不相交：|k_i - k_last| >= m_i + m_last
        if abs(l[i][0] - l[last][0]) >= l[i][1] + l[last][1]:
            last = i
            ans += 1
    return ans


def main(n):
    """
    n 为数据规模，内部生成测试数据并返回结果。
    返回值：最大可选互不相交区间数量。
    """
    data = generate_test_data(n)
    return solve_interval_selection(data)


if __name__ == "__main__":
    # 示例：n = 10
    result = main(10)
    print(result)