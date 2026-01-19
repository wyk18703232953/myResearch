def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def run_algorithm(N, M, Ar):
    pc = [popcount(i) for i in range(1 << (M + 1))]

    inf = 1 << 31
    maxi = [0] * (1 << M)

    for i in range(N):
        a = Ar[i]
        dp = [0] * (1 << M)
        for S in range(1, 1 << M):
            p = pc[S]
            if p == 1:
                k = S.bit_length() - 1
                dp[S] = a[k]
            else:
                dp[S] = min(dp[-S & S], dp[S ^ (-S & S)])
            maxi[S] = max(maxi[S], dp[S])

    for i in range(M):
        for j in range(1 << M):
            if not j & (1 << i):
                maxi[j] = max(maxi[j], maxi[j | (1 << i)])

    D = (1 << M) - 1
    ans = maxi[D]
    aS, bS = D, D
    for S in range(1 << M):
        candi = min(maxi[S], maxi[D ^ S])
        if candi > ans:
            aS, bS = S, D ^ S
            ans = candi

    Ans = [None] * 2
    pre = False
    fro = False

    for i in range(N):
        a = Ar[i]
        resa = inf
        resb = inf
        for j in range(M):
            if (1 << j) & aS:
                resa = min(resa, a[j])
            else:
                resb = min(resb, a[j])
        if resa >= ans:
            pre = True
            Ans[0] = i + 1
        if resb >= ans:
            fro = True
            Ans[1] = i + 1
        if pre and fro:
            break
    return Ans


def main(n):
    if n <= 0:
        n = 1
    M = max(1, n.bit_length() - 1)
    N = max(1, n // max(1, M))

    base = (1 << 30) - 1
    Ar = []
    for i in range(N):
        row = []
        for j in range(M):
            val = base - (i * M + j)
            if val < 0:
                val = 0
            row.append(val)
        Ar.append(tuple(row))

    ans = run_algorithm(N, M, Ar)
    print(*ans)


if __name__ == "__main__":
    main(8)