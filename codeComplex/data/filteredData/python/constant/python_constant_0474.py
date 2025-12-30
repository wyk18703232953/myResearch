import random

def main(n: int):
    # 生成测试数据：n 组 (ax, ay, bx, by, cx, cy)
    # 坐标范围可根据需要调整，这里设为 [-n, n]
    coord_min, coord_max = -n, n

    for _ in range(n):
        ax = random.randint(coord_min, coord_max)
        ay = random.randint(coord_min, coord_max)
        bx = random.randint(coord_min, coord_max)
        by = random.randint(coord_min, coord_max)
        cx = random.randint(coord_min, coord_max)
        cy = random.randint(coord_min, coord_max)

        if ((bx - ax < 0 and cx - ax < 0 or
             bx - ax > 0 and cx - ax > 0) and
            (by - ay < 0 and cy - ay < 0 or
             by - ay > 0 and cy - ay > 0)):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    # 示例：规模 n=5
    main(5)