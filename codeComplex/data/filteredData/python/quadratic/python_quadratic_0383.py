import random


def is_center(a, n, m, y, x):
    count1 = count2 = count3 = count4 = 0

    # up
    y1 = y
    while True:
        y2 = y1 - 1
        if y2 < 0:
            break
        c = a[y2][x]
        if c == "W":
            break
        count1 += 1
        y1 = y2

    # down
    y1 = y
    while True:
        y2 = y1 + 1
        if y2 == n:
            break
        c = a[y2][x]
        if c == "W":
            break
        count2 += 1
        y1 = y2

    # left
    x1 = x
    while True:
        x2 = x1 - 1
        if x2 < 0:
            break
        c = a[y][x2]
        if c == "W":
            break
        count3 += 1
        x1 = x2

    # right
    x1 = x
    while True:
        x2 = x1 + 1
        if x2 == m:
            break
        c = a[y][x2]
        if c == "W":
            break
        count4 += 1
        x1 = x2

    return count1 == count2 == count3 == count4 and a[y][x] == "B"


def generate_grid(n, m):
    # 简单随机生成由 'B' 和 'W' 组成的网格
    chars = ["B", "W"]
    grid = []
    for _ in range(n):
        row = "".join(random.choice(chars) for _ in range(m))
        grid.append(row)
    return grid


def main(n):
    # 设定 m，可根据需要调整，这里设为与 n 相同形成正方形
    m = n

    # 生成测试数据
    a = generate_grid(n, m)

    # 保持与原程序相同的行为：找到第一个中心并输出其位置（1-based）
    for y in range(n):
        found = False
        for x in range(m):
            if is_center(a, n, m, y, x):
                print(y + 1, x + 1)
                found = True
                break
        if found:
            break


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)