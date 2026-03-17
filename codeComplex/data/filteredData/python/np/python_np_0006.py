#!/usr/bin/env python

from itertools import chain
from time import time


def main(n):
    # Interpret n as number of points
    if n < 0:
        n = 0

    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for u, v in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    # Deterministic input generation:
    # Original input format:
    #   line1: ori_x ori_y
    #   line2: N
    #   next N lines: x y
    #
    # Here we construct:
    #   ori = (0, 0)
    #   N = n
    #   pts[i] = (i, i * 2)  for i in 1..N
    ori = (0, 0)
    N = n
    pts = [(i, i * 2) for i in range(1, N + 1)]

    vis = set([0])
    mint = [0] + [1e8] * (1 << N)
    pres = [None] * (1 << N)
    allb = (1 << N) - 1
    B2P = {BITS[u]: v for u, v in enumerate(pts)}
    B2P[0] = ori
    alld = {u: {v: dist(B2P[u], B2P[v]) for v in B2P} for u in B2P}

    getDP = lambda x: mint[x]
    newDist = lambda stt, p: (
        mint[stt]
        + alld[p[0]][p[1]]
        + alld[p[0]][0]
        + alld[p[1]][0]
    )

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

    # print(mint[allb])

    path = ['0']
    stt = allb

    while stt:
        bits = getBits(pres[stt])
        for bit in bits:
            path.append(str(B2N[bit] + 1))
        path.append('0')
        stt ^= pres[stt]

    # print(' '.join(path))


if __name__ == "__main__":
    st = time()
    main(4)
    # print("Run {:.6f} seconds.".format(time() - st))