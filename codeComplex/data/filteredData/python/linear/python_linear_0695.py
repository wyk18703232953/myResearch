from collections import defaultdict as dd
import math
import random


def main(n):
    """
    n: 规模参数，用于生成测试数据
    这里根据 n 生成 n 和 v 的测试值，并执行原逻辑
    """
    # 生成测试数据：
    # 为保证逻辑合理，令 n >= 2
    n_val = max(2, n)
    # v 在 [0, 2*n] 范围内随机生成
    v_val = random.randint(0, 2 * n_val)

    # 原始逻辑开始
    n_input, v = n_val, v_val
    dist = n_input - 1

    if v >= dist:
        result = dist
    else:
        off = dist - v
        prices = [i + 2 for i in range(off)]
        result = v + sum(prices)

    # 返回计算结果及测试数据，方便调试或调用者使用
    return {
        "n": n_input,
        "v": v,
        "result": result
    }


# 示例：直接运行本文件时做一次调用
if __name__ == "__main__":
    output = main(10)
    print(output)