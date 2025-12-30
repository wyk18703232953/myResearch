from itertools import chain
from time import time
import random
import sys

def main(n):
    # n 为点的数量（原程序中的 N）
    # 这里自动生成测试数据：
    # 原点 ori 在 (0,0)
    # 其他 n 个点在 [0, 10]x[0, 10] 的整数网格中随机生成
    random.seed(0)
    ori = (0, 0)
    pts = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(n)]

    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for u, v in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    N = n

    vis = set([0])
    mint = [0] + [1e8] * (1 << N)
    pres = [None] * (1 << N)
    allb = (1 << N) - 1
    B2P = {BITS[u]: v for u, v in enumerate(pts)}
    B2P[0] = ori
    alld = {u: {v: dist(B2P[u], B2P[v]) for v in B2P} for u in B2P}

    getDP = lambda x: mint[x]
    newDist = lambda stt, p: mint[stt] + alld[p[0]][p[1]] + alld[p[0]][0] + alld[p[1]][0]

    for stt in range(1 << N):
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

    print(mint[allb])
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
    st = time()
    # 这里给一个默认规模 n，可根据需要修改
    main(5)
    print('Run {:.6f} seconds.'.format(time() - st), file=sys.stderr)