import random


def main(n):
    # 1) 根据 n 生成测试数据
    # 为了能生成合法数据，需要 w, h, n 功能一致：
    #   - w, h 为整体宽高
    #   - n 为切割次数
    #
    # 生成规则：
    #   - w, h 在 [n+1, 2n+10] 之间，保证至少能切 n 次
    #   - 每一步切割的坐标在 (0, 当前方向长度) 之间
    #   - 交替产生 V / H 切割，使得同时存在纵切和横切
    #
    # 如需特定生成策略，可在此处替换。
    if n <= 0:
        return

    w = n + 10
    h = n + 20

    cuts = []
    for i in range(n):
        # 随机选择纵切或横切
        # 多数情况都有纵横混合
        flag = random.choice(['V', 'H'])
        if flag == 'V':
            # 纵切在 (1, w-1) 内
            x = random.randint(1, w - 1)
        else:
            # 横切在 (1, h-1) 内
            x = random.randint(1, h - 1)
        cuts.append((flag, x))

    # 2) 将原 main 的逻辑改为使用生成的 w, h, n 和 cuts
    res, vrt, hor = [], [], []
    vh = (vrt, hor)

    # 将 cuts 填充到 res，并把索引收集到 vrt / hor
    for i, (c, pos) in enumerate(cuts):
        x = pos
        flag = (c == 'V')  # True 表示纵向切割，对应 vh[1] = hor
        vh[flag].append(i)
        res.append([x, flag])

    dim = []
    # zip(vh, (h, w)): 对应原代码中纵向用 h，横向用 w
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

    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    # 示例：运行规模 n=5
    main(5)