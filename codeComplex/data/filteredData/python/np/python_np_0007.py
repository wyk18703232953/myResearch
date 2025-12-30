import random


def main(n):
    # 生成测试数据：
    # ori: 原点坐标 (3 维)，n 个点：pts
    random.seed(0)
    dim = 3
    ori = tuple(random.randint(0, 10) for _ in range(dim))
    pts = [tuple(random.randint(0, 10) for _ in range(dim)) for _ in range(n)]

    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum((u - v) ** 2 for u, v in zip(ptA, ptB))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    vis = set([0])
    mint = [0] + [1e8] * (1 << n)  # minimal time for dp
    pres = [None] * (1 << n)       # previous step for reconstruct path
    allb = (1 << n) - 1            # all objects contained state
    B2P = {BITS[u]: v for u, v in enumerate(pts)}
    B2P[0] = ori
    alld = {u: {v: dist(B2P[u], B2P[v]) for v in B2P} for u in B2P}

    getDP = lambda x: mint[x]
    newDist = lambda stt, p: mint[stt] + alld[p[0]][p[1]] \
                             + alld[p[0]][0] \
                             + alld[p[1]][0]

    for stt in range(1 << n):
        if stt not in vis:
            continue

        bits = getBits(~stt & allb)

        sb = bits[0] if bits else None

        for bit in bits:
            newstt = stt | sb | bit
            nd = newDist(stt, (sb, bit))
            if getDP(newstt) > nd:
                mint[newstt] = nd
                pres[newstt] = sb | bit
                vis.add(newstt)

    # 输出最小代价
    print(mint[allb])

    # 还原路径
    path = ['0']
    stt = allb

    while stt:
        bits = getBits(pres[stt])
        for bit in bits:
            path.append(str(B2N[bit] + 1))
        path.append('0')
        stt ^= pres[stt]

    print(' '.join(path))


if __name__ == "__main__":
    # 示例：规模 n=4
    main(4)