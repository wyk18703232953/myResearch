import random

def main(n):
    # 生成三个点的坐标，范围可根据 n 调整，这里用 [-n, n]
    ax, ay = random.randint(-n, n), random.randint(-n, n)
    bx, by = random.randint(-n, n), random.randint(-n, n)
    cx, cy = random.randint(-n, n), random.randint(-n, n)

    if ((cx < ax) == (bx < ax)) and ((cy < ay) == (by < ay)):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：可自行修改 n 测试规模
    main(10)