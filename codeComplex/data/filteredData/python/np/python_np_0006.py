#!/usr/bin/env python
from itertools import chain
from time import time
import random
import math

def main(n):
    """
    参数:
        n: 目标点个数 N (原程序中的 N)
    逻辑:
        随机生成 n 个点以及一个原点 ori，点坐标为二维整点。
    返回:
        (best_distance, path_list)
        path_list 为访问顺序，例如 ['0','2','5','0','3','4','0', ...]
    """

    # ========== 测试数据生成 ==========
    # 随机生成 ori 和 n 个点，坐标范围可根据需要调整
    random.seed(0)
    def gen_point():
        return (random.randint(-100, 100), random.randint(-100, 100))

    ori = gen_point()
    pts = [gen_point() for _ in range(n)]
    N = n

    # ========== 原始逻辑开始 ==========
    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for u, v in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    vis = set([0])
    mint = [0] + [1e8] * (1 << N)  # minimal time for dp
    pres = [None] * (1 << N)       # previous step for reconstruct path
    allb = (1 << N) - 1            # all objects contained state
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

    best_dist = mint[allb]
    path = ['0']
    stt = allb

    while stt:
        bits = getBits(pres[stt])
        for bit in bits:
            path.append(str(B2N[bit] + 1))
        path.append('0')
        stt ^= pres[stt]

    # 模拟原来的输出（标准输出），也返回结果
    print(best_dist)
    print(' '.join(path))
    return best_dist, path


if __name__ == '__main__':
    import sys
    st = time()
    # 示例：规模 n=5
    main(5)
    print('Run {:.6f} seconds.'.format(time() - st), file=sys.stderr)