from math import sin, pi

def main(n):
    # 由 n 同时控制多边形边数和半径，保证输入规模含义明确
    # 多边形边数至少为 3
    sides = max(3, n)
    r = n
    R = r * sin(pi / sides) / (1 - sin(pi / sides))
    # print(R)
    pass
if __name__ == "__main__":
    main(10)