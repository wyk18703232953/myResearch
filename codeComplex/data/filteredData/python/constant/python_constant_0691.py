import math
import random

def main(n: int):
    # 根据规模 n 生成测试数据：半径 r
    # 这里简单设定 r = n，或也可用随机数，如：r = random.randint(1, 10 * n)
    r = n

    a = math.pi / n
    sin_val = math.sin(a)
    R = r * sin_val / (1 - sin_val)

    print(R)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)