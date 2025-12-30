import random

def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

def main(n):
    # 规模 n 用来控制 M 和 N，这里做一个合理的生成策略：
    # 让 M 较小，以保证 2^M 不会太大。
    #
    # 示例策略：
    #   M = min(10, max(1, n // 3))
    #   N = n
    #
    # 你可以根据需要修改生成规则。
    M = min(10, max(1, n // 3))
    N = n

    # 生成测试数据 Ar：N 行，每行 M 个整数
    # 数值范围可自行设定，这里设为 1..10^9
    Ar = [
        tuple(random.randint(1, 10**9) for _ in range(M))
        for _ in range(N)
    ]

    pc = [popcount(i) for i in range(1 << (M + 1))]

    inf = 1 << 60
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
                lowbit = S & -S
                dp[S] = min(dp[lowbit], dp[S ^ lowbit])
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

    print(*Ans)


if __name__ == "__main__":
    # 示例：调用 main(9)
    main(9)