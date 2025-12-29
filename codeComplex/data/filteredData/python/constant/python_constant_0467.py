import random

def main(n):
    # 这里的 n 作为“规模”参数，用来控制测试数据生成范围
    # 例如坐标范围设置为 [-n, n]
    coord_min, coord_max = -n, n

    # 随机生成 A, B, C 三个点的坐标
    ax = random.randint(coord_min, coord_max)
    ay = random.randint(coord_min, coord_max)

    bx = random.randint(coord_min, coord_max)
    by = random.randint(coord_min, coord_max)

    cx = random.randint(coord_min, coord_max)
    cy = random.randint(coord_min, coord_max)

    # 原逻辑
    if ((bx < ax and cx < ax) or (bx > ax and cx > ax)) and \
       ((by < ay and cy < ay) or (by > ay and cy > ay)):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：规模设为 10
    main(10)