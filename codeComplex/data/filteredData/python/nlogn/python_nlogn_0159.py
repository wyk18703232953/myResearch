import random


def main(n):
    # 随机生成宽 w、高 h
    w = random.randint(1, 10**9)
    h = random.randint(1, 10**9)

    # 构造 n 条切割指令
    # 每条指令格式: 'V x' 或 'H x'
    # x 为在对应方向上的位置
    cuts = []
    for _ in range(n):
        if random.randint(0, 1) == 0:  # 垂直切割
            x = random.randint(1, w - 1) if w > 1 else 1
            cuts.append(f"V {x}")
        else:  # 水平切割
            x = random.randint(1, h - 1) if h > 1 else 1
            cuts.append(f"H {x}")

    # 以下是原逻辑，仅把 input 替换为上述生成的数据
    res, vrt, hor = [], [], []
    vh = (vrt, hor)
    for i, s in enumerate(cuts):
        x = int(s[2:])
        flag = s[0] == 'V'
        vh[flag].append(i)
        res.append([x, flag])

    dim = []
    for tmp, m in zip(vh, (h, w)):
        tmp.sort(key=lambda e: res[e][0])
        u = [None, [0]]
        dim.append(u)
        j = z = 0
        for i in tmp:
            x = res[i][0]
            if z < x - j:
                z = x - j
            j = x
            v = [u, res[i]]
            u.append(v)
            u = v
            res[i].append(u)
        v = [u, [m], None]
        u.append(v)
        dim.append(v)
        if z < m - j:
            z = m - j
        dim.append(z)

    l, r, wmax, u, d, hmax = dim
    whmax = [wmax, hmax]
    for i in range(n - 1, -1, -1):
        x, flag, link = res[i]
        u = whmax[flag]
        res[i] = u * whmax[not flag]
        link[0][2] = link[2]
        link[2][0] = link[0]
        v = link[2][1][0] - link[0][1][0]
        if u < v:
            whmax[flag] = v

    print("\n".join(map(str, res)))


if __name__ == "__main__":
    # 示例：规模 n=10
    main(10)