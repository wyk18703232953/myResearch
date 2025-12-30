import random

def main(n):
    # n 用作随机数的范围尺度，例如坐标范围 [-n, n]
    coord_min, coord_max = -n, n

    # 随机生成皇后、国王和目标的坐标
    queen_x = random.randint(coord_min, coord_max)
    queen_y = random.randint(coord_min, coord_max)

    king_x = random.randint(coord_min, coord_max)
    king_y = random.randint(coord_min, coord_max)

    tar_x = random.randint(coord_min, coord_max)
    tar_y = random.randint(coord_min, coord_max)

    min_x, max_x = sorted([king_x, tar_x])
    min_y, max_y = sorted([king_y, tar_y])

    if max_x > queen_x > min_x or max_y > queen_y > min_y:
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    # 示例：调用 main(10)，生成范围在 [-10, 10] 内的随机测试数据
    main(10)