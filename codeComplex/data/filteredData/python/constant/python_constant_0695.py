from math import sin, pi
import random

def main(n):
    # 根据规模 n 生成测试数据：
    # 约束：n >= 3，r >= 1
    if n < 3:
        raise ValueError("n 必须 >= 3")
    r = random.randint(1, 1000)

    R = r * sin(pi / n) / (1 - sin(pi / n))
    print(R)

if __name__ == "__main__":
    # 示例：使用 n = 6 运行
    main(6)