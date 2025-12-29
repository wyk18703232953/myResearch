import sys
import math
import random

sys.setrecursionlimit(1000000)


def main(n: int):
    """
    n 为规模，对应原程序中的 N。
    根据 n 构造测试数据，并执行原逻辑。
    """
    # 原程序逻辑开始
    N = n
    re = 0
    for i in range(2, N):
        t = N // i - 1
        re += t * i
    result = re * 4
    # 原程序仅输出结果
    print(result)


if __name__ == "__main__":
    # 这里根据规模 n 生成测试数据
    # 示例策略：直接使用传入的规模作为 N；
    # 如需更复杂的随机数据，可在此修改。
    test_n = 10  # 示例：可修改或由外部调用 main(n)
    main(test_n)