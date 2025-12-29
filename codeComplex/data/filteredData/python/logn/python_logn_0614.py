import math
import random


def main(n):
    # 生成测试数据：随机生成 1 <= k <= n*(n+1)//2
    # 原题场景一般是关于前缀和 / 三角数之类的问题，这里按该规模生成合理范围的 k
    max_k = n * (n + 1) // 2
    if max_k <= 0:
        return  # n 非正时无意义，直接返回
    k = random.randint(1, max_k)

    # 原逻辑
    temp = 2 * (k + n)
    m = (-3 + math.sqrt(9 + 4 * temp)) / 2
    print(int(n - m))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)