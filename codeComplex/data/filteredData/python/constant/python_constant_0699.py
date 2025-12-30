import math
import random

def main(n: int):
    """
    n: 规模，用来生成测试数据
       例如：N 取为 n，r 取为 1 到 n 范围内的随机整数
    """
    if n < 3:
        raise ValueError("n 必须 >= 3 才能形成多边形")

    # 根据规模 n 生成测试数据
    N = n
    r = random.randint(1, n)

    # 原公式：sin(360/N) = R / (r + R)
    # 输出：r * sin(pi/N) / (1 - sin(pi/N))
    result = r * math.sin(math.pi / N) / (1 - math.sin(math.pi / N))
    print(result)


if __name__ == "__main__":
    # 可在此处指定一个默认规模进行测试
    main(10)