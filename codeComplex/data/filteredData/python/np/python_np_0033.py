def main(n):
    import random

    mod = 10**9 + 7

    # 生成测试数据：N = n，A 中元素为 [0, 2^20) 内随机整数
    N = n
    m = 20
    M = 1 << m
    A = [random.randrange(M) for _ in range(N)]

    F = [0] * M
    for a in A:
        F[a] += 1

    def zeta_transform(F, nbit):
        # res[i] = (i を含む集合 j に対する F[j] の和)
        NN = 1 << nbit
        res = F[:]
        for i in range(nbit):
            k = 1 << i
            for j in range(NN):
                if not j & k:
                    res[j] += res[j ^ k]
        return res

    G = zeta_transform(F, m)

    power = [1]
    for _ in range(N):
        power.append((power[-1] * 2) % mod)

    def bit_count(x):
        c = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
        c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
        c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
        c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
        c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
        c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
        return c

    ans = 0
    for i in range(M):
        bc = bit_count(i)
        a = power[G[i]]
        if bc % 2 == 0:
            ans += a
        else:
            ans -= a
        ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例：规模 n = 5
    main(5)