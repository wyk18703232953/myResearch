def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def main(n):
    if n < 2:
        n = 2
    # Define M and N as functions of n to scale the problem size.
    # M controls bitmask size (2^M states), N is number of rows.
    M = max(1, n // 2)
    N = max(1, n)

    # Deterministic generation of Ar: N rows, each with M integers
    # Values are simple deterministic functions of (i, j)
    Ar = [tuple((i + 1) * (j + 2) % 1000000007 for j in range(M)) for i in range(N)]

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
                low = -S & S
                dp[S] = min(dp[low], dp[S ^ low])
            maxi[S] = max(maxi[S], dp[S])

    for i in range(M):
        bit = 1 << i
        for j in range(1 << M):
            if not j & bit:
                maxi[j] = max(maxi[j], maxi[j | bit])

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

    print(Ans[0], Ans[1])


if __name__ == "__main__":
    main(8)