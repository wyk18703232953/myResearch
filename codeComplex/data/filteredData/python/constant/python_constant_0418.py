import random

def main(n: int):
    # 生成规模为 n 的测试数据（这里的 n 不直接用于原逻辑，
    # 仅用来控制坐标的随机范围 [-n, n]）
    coords1 = [random.randint(-n, n) for _ in range(8)]
    coords2 = [random.randint(-n, n) for _ in range(8)]

    x1, y1, x2, y2, x3, y3, x4, y4 = coords1
    x11, y11, x22, y22, x33, y33, x44, y44 = coords2

    min_x1 = min(x1, x2, x3, x4)
    min_y1 = min(y1, y2, y3, y4)
    max_x1 = max(x1, x2, x3, x4)
    max_y1 = max(y1, y2, y3, y4)

    min_x11 = min(x11, x22, x33, x44)
    min_y11 = min(y11, y22, y33, y44)
    max_x11 = max(x11, x22, x33, x44)
    max_y11 = max(y11, y22, y33, y44)

    a = (max_x11 + min_x11) / 2
    b = (max_y11 + min_y11) / 2
    d2 = (max_x11 - min_x11) / 2

    for x in range(min_x1, max_x1 + 1):
        for y in range(min_y1, max_y1 + 1):
            if abs(x - a) + abs(y - b) <= d2:
                print("yes")
                return
    print("no")


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)