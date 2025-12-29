import math
import random

def main(n: int):
    # 根据规模 n 生成测试数据，这里示例为在 [1, n] 内随机生成一个整数
    num = random.randint(1, n)

    k = math.ceil(num / 2)
    if num % 2 == 0:
        print(k + 1)
    else:
        print(k)


if __name__ == "__main__":
    # 示例：将规模 n 设为 100
    main(100)