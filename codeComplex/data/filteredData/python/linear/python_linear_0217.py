def main(n):
    # n 表示点的数量
    # 构造确定性的 a, b
    a = n % 10 + 1
    b = (n // 10) % 10 + 1

    dc = {}
    for i in range(n):
        # 确定性生成 x, vx, vy
        x = i
        vx = (i % 7) - 3      # 在 [-3,3] 内
        vy = (i % 11) - 5     # 在 [-5,5] 内

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
    # print(tot)
    pass
if __name__ == "__main__":
    main(10)