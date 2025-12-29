import math
import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里令 k 为 1 到 3n 之间的随机正整数（避免 k 过小或为 0）
    if n <= 0:
        raise ValueError("n must be positive")
    k = random.randint(1, 3 * n)

    # 原逻辑：
    # print((-(-n*2//k))+(-(-n*5//k))+(-(-n*8//k)))
    # 使用 math.ceil 更直观
    part1 = math.ceil(n * 2 / k)
    part2 = math.ceil(n * 5 / k)
    part3 = math.ceil(n * 8 / k)
    result = part1 + part2 + part3

    print(result)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)