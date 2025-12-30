# -*- coding: utf-8 -*-
"""
LCM Challenge - 参数化版本
根据规模 n 生成测试数据，并计算题目要求的答案。
原题链接：https://codeforces.com/problemset/problem/235/A
"""

def solve(n: int) -> int:
    """
    原始逻辑封装为函数：
    对给定的 n 计算题目中要求的最大 lcm(a, b, c)（化简后的公式版本）。
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n % 2 == 0:
        if n % 3 == 0:
            return (n - 1) * (n - 2) * (n - 3)
        else:
            return n * (n - 1) * (n - 3)
    else:
        return n * (n - 1) * (n - 2)


def main(n: int):
    """
    主函数：
    1. 使用传入的规模 n 作为“测试数据”。
    2. 计算并打印答案。
    """
    ans = solve(n)
    print(ans)


# 示例：如需本地测试，可手动调用 main(n)
# main(10)