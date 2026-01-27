from math import sin

pi = 3.141592653589793238462643383279502884197

def main(n):
    # 解释规模含义：
    # n >= 3：多边形边数 n，半径 r = n
    # n < 3：退化情形，直接返回 0.0
    if n < 3:
        # print(0.0)
        pass
        return
    r = float(n)
    theta = 2 * pi / n
    R = r / (1 - sin(theta / 2))
    # print(R - r)
    pass
if __name__ == "__main__":
    main(10)