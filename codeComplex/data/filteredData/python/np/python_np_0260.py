import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 3 个矩形，每个边长在 1..n 之间
    # 数据格式与原程序一致：a b c d e f
    a = random.randint(1, n)
    b = random.randint(1, n)
    c = random.randint(1, n)
    d = random.randint(1, n)
    e = random.randint(1, n)
    f = random.randint(1, n)

    # 原程序逻辑开始
    if a < b:
        a, b = b, a
    if c < d:
        c, d = d, c
    if e < f:
        e, f = f, e

    sides = [[a, b, 'A'], [c, d, 'B'], [e, f, 'C']]
    sides.sort(reverse=True)
    c1, c2, c3 = sides[0][2], sides[1][2], sides[2][2]
    area = a * b + c * d + e * f

    if int(area ** 0.5) ** 2 != area:
        print(-1)
        return

    l = int(area ** 0.5)
    if l not in sides[0]:
        print(-1)
        return

    if l in sides[1] and l in sides[2]:
        print(l)
        for i in range(3):
            sides[i].remove(l)
        for i in range(3):
            for _ in range(sides[i][0]):
                print([c1, c2, c3][i] * l)
    else:
        r = l - sides[0][1]
        if r in sides[1] and r in sides[2]:
            print(l)
            for i in range(1, 3):
                sides[i].remove(r)
            for _ in range(sides[0][1]):
                print(c1 * l)
            for _ in range(r):
                print(c2 * sides[1][0] + c3 * sides[2][0])
        else:
            print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)