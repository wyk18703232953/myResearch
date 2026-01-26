import math

def main(n):
    # 映射：原程序中 n 为多边形边数，r 为内切圆半径
    # 这里将输入规模参数 N 同时映射为 n 和 r，保证算法结构不变
    if n <= 1:
        return 0.0
    sides = n
    r = float(n)

    angle = math.pi / sides
    sin_val = math.sin(angle)
    R = r * sin_val / (1 - sin_val)
    return R

if __name__ == "__main__":
    # 示例调用：可根据需要调整 n 的大小进行时间复杂度实验
    result = main(1000)
    # print(result)
    pass