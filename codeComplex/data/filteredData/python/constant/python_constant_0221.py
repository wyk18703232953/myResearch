import random

def main(n: int):
    # 生成测试数据
    # yellow, blue 在 [0, n]
    yellow = random.randint(0, n)
    blue = random.randint(0, n)
    # x, y, z 在 [0, n]
    x = random.randint(0, n)
    y = random.randint(0, n)
    z = random.randint(0, n)

    ry = x * 2 + y
    rb = z * 3 + y
    r1, r2 = 0, 0

    if ry - yellow < 0:
        r1 = 0
    else:
        r1 = ry - yellow

    if rb - blue < 0:
        r2 = 0
    else:
        r2 = rb - blue

    print(r1 + r2)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)