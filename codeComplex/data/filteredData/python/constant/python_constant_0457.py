import random

def main(n: int):
    # 生成三组点坐标 (ax, ay), (bx, by), (cx, cy)
    # 坐标范围可根据 n 调整，这里使用 [1, n]
    ax, ay = random.randint(1, n), random.randint(1, n)
    bx, by = random.randint(1, n), random.randint(1, n)
    cx, cy = random.randint(1, n), random.randint(1, n)

    x = [ax, bx, cx]
    y = [ay, by, cy]

    x.sort()
    y.sort()

    if (x[1] != ax) and (y[1] != ay):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    # 示例：n = 10
    main(10)