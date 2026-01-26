import math

def main(n):
    # 在原程序中，n 是多边形边数，r 是半径
    # 这里将输入规模参数 n 用作多边形边数
    # 半径 r 采用一个确定性的固定值
    r = 10

    if n <= 1:
        # 避免除以 0 或无意义输入
        # print("0.0000000")
        pass
        return

    s = math.sin(math.pi / n)
    ans = (r * s) / (1 - s)

    # print(f"{ans:.7f}")
    pass
if __name__ == "__main__":
    main(1000)