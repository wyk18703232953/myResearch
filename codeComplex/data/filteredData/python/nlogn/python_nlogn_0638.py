def main(n):
    # 这里的 n 同时作为竖线数量与横线数量的规模参数
    # 你可以按需要调整横线数量的生成方式
    import random

    # 生成测试数据：竖线 vert，长度为 n，取值在 [1, 1e9]
    vert = sorted(random.randint(1, 10**9) for _ in range(n))

    # 生成测试数据：横线 horiz，长度为 n
    # 每条横线格式为 (y, x1, x2)，按原题逻辑，只在 x1 == 1 时加入 hh
    horiz = []
    for _ in range(n):
        y = random.randint(1, 10**9)
        # 为了产生有效的 x1 == 1 的情况，随机生成少量 x1==1 的线段
        if random.random() < 0.5:
            x1 = 1
        else:
            x1 = random.randint(2, 10**9)
        x2 = random.randint(x1, 10**9)
        horiz.append((y, x1, x2))

    # 按原程序逻辑进行计算
    horiz.sort()

    p = -1
    hh = []
    for y, x1, x2 in horiz:
        if p != y:
            p = y
            if x1 == 1:
                hh.append(x2)

    hh.sort()
    i = 0
    hl = len(hh)
    vl = len(vert)
    r = len(vert) + len(horiz)

    for j in range(vl):
        while i < hl and hh[i] < vert[j]:
            i += 1
        r = min(r, hl - i + j)

    while i < hl and hh[i] < 1000000000:
        i += 1
    r = min(r, hl - i + vl)

    print(r)


if __name__ == "__main__":
    # 示例运行：使用 n = 10 作为规模
    main(10)