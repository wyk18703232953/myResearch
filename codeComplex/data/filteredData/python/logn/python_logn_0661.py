import math
import random

def main(n):
    # 1. 生成规模为 n 的测试数据：
    #    原程序中有 n 和 k 两个输入，这里固定 n，随机生成一个合理范围内的 k
    #    根据原公式中的判别式约束，k 的量级大致在 O(n^2) 内是合理的
    k = random.randint(0, n * n)

    # 2. 按原逻辑计算 m1
    if (3 + 2 * n + math.sqrt((3 + 2 * n) ** 2 - 4 * (n + n * n - 2 * k))) / 2 < n:
        m1 = (3 + 2 * n + math.sqrt((3 + 2 * n) ** 2 - 4 * (n + n * n - 2 * k))) / 2
    else:
        m1 = (3 + 2 * n - math.sqrt((3 + 2 * n) ** 2 - 4 * (n + n * n - 2 * k))) / 2

    print(int(m1))


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)