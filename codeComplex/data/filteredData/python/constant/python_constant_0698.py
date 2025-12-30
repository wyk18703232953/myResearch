from math import pi, sin
import random

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 原程序中 n 为多边形边数，r 为半径，这里按题意将两个量都由规模 n 决定
    # 约定：多边形边数 sides = max(3, n)，半径 r = float(n)
    sides = max(3, n)
    r = float(n)

    ang = pi / sides
    k = sin(ang)
    result = k * r / (1 - k)
    print(result)

if __name__ == "__main__":
    # 示例：用 n=10 作为规模运行
    main(10)