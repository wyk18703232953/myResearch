from math import sqrt
import random


def main(n):
    # 生成测试数据：
    # 原代码中有 n, k 两个参数，这里根据规模 n 随机生成一个 k
    # 你可以根据实际需求修改生成方式
    k = random.randint(0, max(1, 2 * n))

    # 原始逻辑
    answer = int(-1.5 + sqrt(9 / 4 + 2 * (n + k)))
    result = n - answer

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(100) 作为测试
    main(100)