from math import sin
import random

pi = 3.141592653589793238462643383279502884197

def main(n: int):
    # 根据规模 n 生成测试数据：
    # 为了与原程序兼容，这里让多边形边数为 n，半径 r 作为一个与 n 同尺度的随机整数
    # 若需固定 r，也可以直接设定为常数
    r = random.randint(1, max(1, n * 10))

    theta = 2 * pi / n
    R = r / (1 - sin(theta / 2))
    print(R - r)


if __name__ == "__main__":
    # 示例：调用 main(6) 代表原来输入中的 n=6，r 自动生成
    main(6)