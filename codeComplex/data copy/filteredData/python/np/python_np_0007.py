import sys


def main(n):
    # n controls the number of points
    if n < 1:
        n = 1
    N = n

    BITS = [1 << sh for sh in range(24)]
    B2N = {v: u for u, v in enumerate(BITS)}

    # Deterministic generation of origin and points
    # Origin point in 2D
    ori = (0, 0)

    # Generate N points in 2D deterministically based on n
    pts = []
    for i in range(1, N + 1):
        # Simple deterministic coordinates; depend only on i
        x = i
        y = i * 2
        pts.append((x, y))

    def dist(ptA, ptB):
        return sum(((u - v) ** 2 for u, v in zip(ptA, ptB)))

    def getBits(val):
        return tuple(filter(lambda x: x & val, BITS))

    vis = set([0])
    mint = [0] + [1e8] * (1 << N)  # minimal time for dp
    pres = [None] * (1 << N)  # previous step for reconstruct path
    allb = (1 << N) - 1  # all objects contained state
    B2P = {BITS[u]: v for u, v in enumerate(pts)}
    B2P[0] = ori
    alld = {u: {v: dist(B2P[u], B2P[v]) for v in B2P} for u in B2P}

    getDP = lambda x: mint[x]
    newDist = lambda stt, p: mint[stt] + alld[p[0]][p[1]] \
                             + alld[p[0]][0] \
                             + alld[p[1]][0]

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
    # Example deterministic call; adjust n to test different scales
    main(4)