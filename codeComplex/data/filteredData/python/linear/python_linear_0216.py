def main(n):
    import random

    # 生成测试数据
    # 生成随机 a, b
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # 生成 n 组 (x, vx, vy)
    # 数值范围可根据需要调整
    xs = []
    for _ in range(n):
        x = random.randint(-10**6, 10**6)
        vx = random.randint(-10**6, 10**6)
        vy = random.randint(-10**6, 10**6)
        xs.append((x, vx, vy))

    dc = {}
    for x, vx, vy in xs:
        nx = x + vx
        ny = a * x + b + vy
        dd = a * nx - ny + b
        if dd not in dc:
            dc[dd] = {}
        if (vx, vy) not in dc[dd]:
            dc[dd][(vx, vy)] = 0
        dc[dd][(vx, vy)] += 1

    tot = 0
    for _, k in dc.items():
        tt = 0
        pp = 0
        for _, cc in k.items():
            tt -= cc * (cc + 1) // 2
            pp += cc
        tt += pp * (pp + 1) // 2
        tot += tt * 2

    print(tot)


if __name__ == '__main__':
    # 示例: 以 n = 10 运行
    main(10)