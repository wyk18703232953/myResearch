import math
import random

def main(n: int):
    # 生成测试数据：随机生成一个半径 r，范围 [1, 100]
    r = random.uniform(1.0, 100.0)

    # 原始计算逻辑
    result = r / (1 / math.cos(math.pi * (n - 2) / (2 * n)) - 1)

    print(result)

if __name__ == "__main__":
    # 示例：调用 main，规模 n 由此处指定
    main(6)