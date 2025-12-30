import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里假设原题中 n, k 为正整数，且 k 不超过 n 的量级
    # 可根据需要调整生成策略
    k = random.randint(0, max(1, n))

    # 原逻辑
    t = math.ceil(math.sqrt(2 * (n + k) + 2.25) - 1.5)
    result = n - t

    print(result)


if __name__ == "__main__":
    # 示例：调用 main(10)，可以自行修改或在外部调用 main
    main(10)