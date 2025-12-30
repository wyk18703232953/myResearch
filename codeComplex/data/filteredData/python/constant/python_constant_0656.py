import random

def main(n: int):
    # 生成测试数据：根据规模 n 控制坐标范围
    # 坐标绝对值不超过 n
    xa = random.randint(-n, n)
    ya = random.randint(-n, n)
    xb = random.randint(-n, n)
    yb = random.randint(-n, n)
    xc = random.randint(-n, n)
    yc = random.randint(-n, n)

    # 为了更稳定的测试，可以取消上面随机改为固定生成规则，例如：
    # xa, ya = 0, 0
    # xb, yb = n // 2, n // 3
    # xc, yc = n, n // 2

    # 原始逻辑开始
    if (xb, yb) < (xa, ya):
        xa, ya, xb, yb = xb, yb, xa, ya
    if (xc, yc) < (xa, ya):
        xa, ya, xc, yc = xc, yc, xa, ya
    if xb > xc:
        xb, yb, xc, yc = xc, yc, xb, yb
    d = 1 if ya <= yc else -1
    if ya <= yb <= yc or ya >= yb >= yc:
        print(xc - xa + abs(yc - ya) + 1)
        for x in range(xa, xb):
            print(x, ya)
        for y in range(ya, yc, d):
            print(xb, y)
        for x in range(xb, xc + 1):
            print(x, yc)
    elif yb < min(ya, yc):
        print(xc - xa + max(ya, yc) - yb + 1)
        for x in range(xa, xc + 1):
            print(x, min(ya, yc))
        for y in range(yb, min(ya, yc)):
            print(xb, y)
        if ya < yc:
            for y in range(ya + 1, yc + 1):
                print(xc, y)
        else:
            for y in range(yc + 1, ya + 1):
                print(xa, y)
    else:
        print(xc - xa + yb - min(ya, yc) + 1)
        for x in range(xa, xc + 1):
            print(x, max(ya, yc))
        for y in range(max(ya, yc) + 1, yb + 1):
            print(xb, y)
        if ya < yc:
            for y in range(ya, yc):
                print(xa, y)
        else:
            for y in range(yc, ya):
                print(xc, y)


if __name__ == "__main__":
    # 示例调用，规模可自行修改
    main(10)