import sys

mod = 10**9 + 7


def zeta_transform(F, n):
    N = 1 << n
    res = F[:]
    for i in range(n):
        k = 1 << i
        for j in range(N):
            if not j & k:
                res[j] += res[j ^ k]
    return res


def bit_count(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


def main(n):
    # Interpret n as the number of elements N in the original program.
    # Each A[i] is a deterministic integer in [0, 2^20).
    N = n
    m = 20
    M = 1 << m

    A = [(i * 17 + 23) % M for i in range(N)]

    F = [0] * M
    for a in A:
        F[a] += 1

    G = zeta_transform(F, m)

    power = [1]
    for _ in range(N):
        power.append((power[-1] * 2) % mod)

    ans = 0
    for i in range(M):
        bc = bit_count(i)
        a = power[G[i]] if G[i] <= N else pow(2, G[i], mod)
        if bc % 2 == 0:
            ans += a
        else:
            ans -= a
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main(10)