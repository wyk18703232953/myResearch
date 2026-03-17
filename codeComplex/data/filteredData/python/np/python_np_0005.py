from itertools import chain
from time import time

def main(n):
    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for u, v in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    def chooseTwo(pool):
        nn = len(pool)
        for i in range(nn):
            for j in range(i + 1, nn):
                yield (pool[i], pool[j])

    # Deterministic data generation based on n
    # Interpret n as number of points N (0 <= N <= 24)
    N = max(0, min(24, int(n)))
    ori = (0, 0)
    pts = [(i, i + 1) for i in range(1, N + 1)]

    vis = set([0])
    mint = [0] + [1e8] * (1 << N)
    pres = [None] * (1 << N)
    allb = (1 << N) - 1
    B2P = {BITS[u]: v for u, v in enumerate(pts[:N])}
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

    # print(mint[allb] if allb >= 0 else 0)
    path = ['0']
    stt = allb

    while stt:
        bits = getBits(pres[stt])
        for bit in bits:
            path.append(str(B2N[bit] + 1))
        path.append('0')
        stt ^= pres[stt]

    # print(' '.jwoin(path))


if __name__ == "__main__":
    st = time()
    main(10)
    import sys
    print('Run {:.6f} seconds.'.format(time() - st), file=sys.stderr)