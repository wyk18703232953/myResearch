import math

def main(n):
    # 约定：n 为圆的数量；半径 r 固定为 1
    r = 1
    # 生成确定性的横坐标，间隔为 1
    x = list(range(n))
    y = [r]

    for i in range(1, n):
        _y = r
        for j in range(i):
            dx = x[i] - x[j]
            if 4 * r * r >= dx * dx:
                candidate = y[j] + math.sqrt(4 * r * r - dx * dx)
                if candidate > _y:
                    _y = candidate
        y.append(_y)

    # print(' '.join(map(str, y)))
    pass
if __name__ == "__main__":
    main(10)