from math import pi, sin

def main(n):
    # 将 n 解释为多边形边数，半径 r 也由 n 确定性生成
    # 保证 n 至少为 3，以避免几何退化
    if n < 3:
        n = 3
    sides = float(n)
    r = float(n)  # 半径与 n 相同，确定性构造
    ang = pi / sides
    k = sin(ang)
    result = k * r / (1 - k)
    # print(result)
    pass
if __name__ == "__main__":
    main(10)