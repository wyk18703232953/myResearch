import random

def main(n):
    # 生成测试数据：A, C 以及 n 行 (z, x, y)
    # 可按需要修改生成规则
    A = random.randint(1, 10)
    C = random.randint(1, 10)

    def Ro(x, y):
        return A * x - y + C

    huh = []
    for _ in range(n):
        # 生成 z, x, y，范围可调整
        z = random.randint(-10, 10)
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        huh.append((Ro(x + z, z * A + y), x))

    huh = sorted(huh)
    anss = 0
    c1 = 0
    c2 = 0
    prev = (-9999999999999, -999999999999999)
    g = []

    huh.append((-9999999999999, -999999999999999))

    for huhh in huh:
        if huhh[0] != prev[0]:
            g.append(c1)
            for j in g:
                anss += (c2 - j) * j
            g = []
            c1 = 1
            c2 = 1
            prev = (huhh[0], huhh[1])
            continue
        c2 += 1
        if huhh[1] != prev[1]:
            g.append(c1)
            c1 = 0
            prev = (huhh[0], huhh[1])
        c1 += 1

    print(anss)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)