def main(n: int):
    import random

    # 生成测试数据
    # 参数范围可按需要调整
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)

    # 随机生成 n 组 (x, vx, vy)
    # 为避免数值过大，这里限制在较小范围
    data = []
    for _ in range(n):
        x = random.randint(-10**4, 10**4)
        vx = random.randint(-10**4, 10**4)
        vy = random.randint(-10**4, 10**4)
        data.append((x, vx, vy))

    # 原逻辑
    dc = {}
    for x, vx, vy in data:
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


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)