from math import sqrt
import random


def main(n):
    """
    n: 规模参数，用来生成测试数据。
       我们这里约定：
       - k 在 1 到 n*(n+1)//2 的范围内随机生成
    程序最终只打印结果 res。
    """
    # 生成测试数据
    # 保证 k 不超过原公式中 n*(n+1)//2 的最大值
    max_k = max(1, n * (n + 1) // 2)
    k = random.randint(1, max_k)

    # 原逻辑开始
    a = 1
    b = -1 * (2 * n + 3)
    c = n * (n + 1) - 2 * k

    res = (-1 * b) - sqrt((b * b) - 4 * a * c)
    res = res / 2
    res = int(res)
    print(res)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)